import io
import os
import pyzipper
import traceback
import aiohttp
import aiofiles
import asyncio

from Crypto.Cipher import AES
from aiohttp import web

scoreboard_host = os.environ.get('SCOREBOARD', '127.0.0.1')
bind_host = os.environ.get('HOST', '127.0.0.1')

MAX_HIST = 3000
MAX_SIZE = 1024
FAILED_SCORE = 9999
score, history = 0, []
#round, key, flag, correct = 0, None, None, False
#round, key, flag, correct = 0, b'\0' * 16, b'\0'*32, False

def pad(m):
    padlen = -len(m) % 16
    return m + bytes([0] * padlen)

round, key, correct = 0, b'a' * 16, False
flag = b'a' * 16
#flag += 'GTF{Nc4T:_c0nNec7iON_r3fuSEd.}'.encode()
flag += 'GTF{我看倒有點像稿紙。}'.encode()
#flag += '🚗{有位帥哥開著一輛敞篷的賓士😎😎一手握著方向盤還一手拿沙士🍺🍺又飛過一輛閃閃發亮的ＢＭＷ}'.encode()
#flag += 'GTF{hello world!}'.encode()
#flag += 'GTF{from pwn import *}'.encode()
#flag += 'GTF{こんばんは！}'.encode()
#flag += 'JOJO{オラオラオラオラオラオラ}'.encode()
#flag += 'GTF{안녕하십니까}'.encode()
print(flag)
flag = pad(flag)

# oalieno
aes = AES.new(key, AES.MODE_CBC, flag[:16])
flag = flag[:16] + aes.encrypt(flag[16:])

routes = web.RouteTableDef()


def check_flag():
    if flag is None or key is None or round < 0:
        raise web.HTTPServiceUnavailable()


@routes.get('/admin/next_round')
async def _(req):
    global round, key, flag, correct, history, score

    try:
        token = req.query['token']
        assert token == req.app['scoreboard_token']
    except Exception:
        raise web.HTTPForbidden()

    try:
        new_round = int(req.query['round'])
        new_key = bytes.fromhex(req.query['key'])
        new_flag = bytes.fromhex(req.query['flag'])
        assert len(new_key) == 16
        assert len(new_flag) > 16
        assert len(new_flag) % 16 == 0
        old_score = FAILED_SCORE if not correct else min(FAILED_SCORE, score)
        old_history = history
        old_correct = correct
    except Exception:
        raise web.HTTPBadRequest()

    print(f'[+] New round {new_round}')
    # print(f'[+] New round {new_round} {new_key.hex()} {new_flag.hex()}')
    round, key, flag, correct, history, score = new_round, new_key, new_flag, False, [], 0

    return web.json_response({'correct': old_correct, 'history': old_history, 'score': old_score})


@routes.get('/status')
async def _(req):
    check_flag()

    return web.json_response({'round': round, 'correct': correct, 'score': score, 'flag': flag.hex()})


@routes.get('/compress')
async def _(req):
    global score
    check_flag()

    try:
        data = bytes.fromhex(req.query['x'])
        assert 16 < len(data) <= MAX_SIZE
        assert len(data) % 16 == 0
    except Exception:
        raise web.HTTPBadRequest()

    aes = AES.new(key, AES.MODE_CBC, data[:16])
    ptxt = aes.decrypt(data[16:]).strip(b'\0')

    score += 1
    if len(history) < MAX_HIST:
        history.append([0, data.hex()])

    out = io.BytesIO()
    with pyzipper.AESZipFile(out,
                             'w',
                             compression=pyzipper.ZIP_LZMA,
                             encryption=pyzipper.WZ_AES) as zf:
        zf.setpassword(key)
        zf.writestr('flag', ptxt)
    
    print(ptxt, len(out.getvalue()))

    return web.Response(
        headers={'Content-Disposition': 'Attachment; filename=flag.zip'},
        body=out.getvalue())


@routes.get('/submit')
async def _(req):
    global correct, score

    check_flag()

    try:
        data = req.query['x'].encode('utf8')
    except Exception:
        raise web.HTTPBadRequest()

    score += 1
    if len(history) < MAX_HIST:
        history.append([1, data.hex()])

    aes = AES.new(key, AES.MODE_CBC, flag[:16])
    ptxt = aes.decrypt(flag[16:]).strip(b'\0')

    if data == ptxt:
        correct = True

    return web.Response(text='⊂((・▽・))⊃' if data == ptxt else '（ ´థ౪థ） ( ´థ,_‥థ｀)')


@routes.get('/')
async def _(req):
    return aiohttp.web.HTTPFound('/index.html')


routes.static('/', './')



@web.middleware
async def error_middleware(request, handler):
    resp = web.HTTPInternalServerError()
    try:
        resp = await handler(request)
    except web.HTTPException as ex:
        resp = ex
    except:
        traceback.print_exc()
        resp = web.HTTPInternalServerError()
    if resp is None or resp.status < 400:
        return resp
    if resp.status == 403:
        raise web.HTTPForbidden(text='( ･∀･)つ＝≡≡ξ)Д`)')
    if resp.status == 404:
        raise web.HTTPNotFound(text='(ﾟヘﾟ)')
    if resp.status < 500:
        raise web.HTTPBadRequest(text='¯\_༼ ಥ ‿ ಥ ༽_/¯')
    if resp.status == 503:
        raise web.HTTPServiceUnavailable(text=''
            'Congrats\n'
            'You might have crashed the server.\n'
            'There is no flag on this server now.\n'
            '(σﾟ∀ﾟ)σﾟ∀ﾟ)σﾟ∀ﾟ)σ\n'
            '(σﾟ∀ﾟ)σﾟ∀ﾟ)σﾟ∀ﾟ)σ\n'
            '(σﾟ∀ﾟ)σﾟ∀ﾟ)σﾟ∀ﾟ)σ\n'
            '(σﾟ∀ﾟ)σﾟ∀ﾟ)σﾟ∀ﾟ)σ\n'
            '\n'
            'Please contact admin if you stop all your exploits\n'
            'but the problem still exists in the next round.\n'
            )
    raise web.HTTPInternalServerError(text='((((；ﾟДﾟ)))')


async def get_scoreboard_token(app):
    async with aiohttp.ClientSession() as sess:
        while True:
            try:
                async with sess.get(f'http://{scoreboard_host}:31337/token') as res:
                    app['scoreboard_token'] = await res.text()
            except Exception:
                traceback.print_exc()
                print('')
                await asyncio.sleep(1)
            else:
                break


app = web.Application(middlewares=[error_middleware])
#app.on_startup.append(get_scoreboard_token)
app.add_routes(routes)
web.run_app(app, host=bind_host, port=11337)
