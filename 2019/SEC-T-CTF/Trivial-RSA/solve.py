#!/usr/bin/env sage
from Crypto.Util.number import *
from gmpy2 import isqrt

n = [16665162598091416675035243372929255215330237988600063606115453406246759269279788760269977993441302227754535063989940158801403082299136924692382379772238783511717805089453627769958409474798262234585212880036578100065244955419654350030210214612873050000707217728997449651244785327256673209001617229204596903739745000294771409411741050416912250410842101344110865361910624576900847453308353320549785990249062848385268654951594713494728031930339317011245422247813046177464952338694367015023462166849724348822067012372916419798329882575892837697474973759070677459272935998500533063881083981623170007582400032456357369057331, 12327967666608400089684292637697723886692743047311943117634453297696672596602132832770180763706410481136385428797064430470744303260875130025364968184033440278168149230015012651339700361911455246276535179299003908649820055478166532502332896978314839548456221498409689020137730201961802661796522959185289676293168958100994789278927928614060667061494784764996405812503722093377901735054396731379083755482112808051044511509930814761992548239396939638987562480503407989092943629763956630828533555667490559450650474172687439499014071217245302164885369990725379389835929411041979972161099398047802667999958241746711037377019]

x = [651462892194717457221755220174856890047929116650078860763950453454949587828096234616831315488704251531401792609600066162972268247282594239275742779598127716518383086923760296725577120504817396207799394031948181614036825015620143890966541423830037471615505961486852765107641800802598611031433822941186606730, 442296418993240063675266142454740191465599525570774611710139968474930425844945295951472133337584882919079119792948035796322583493017921438477858246253211352232247225094327539626813294415765610979636199753519138117254187197466480294243789769005210602152862859358315543589192060482998253522480707816974954144]

cipher = 7899134322955645246464106475661567371519411492907819361218537936109003314263398594946847506479710018156056516572597388680265129465680577498126784603599657304217232946737359907830193767343579320119617475061103397775839997585822041520474984253434505877605909867411822079954503549880731554010164405517963598831678530319685550356656748243909520671642189043288332595811057445820791781035731118992393238366930032136586970961554635691292784903624264141333213116074342104788426932419021114413087179933685563867060402709899375500659953038354210747849030819495299042436380277429490866466199179979698665821921998413237763283416

def solve(n, x):
    a = x[1]
    b = n[0] - n[1] + x[0] * x[1]
    c = x[0] * n[0]
    discriminant = b * b - 4 * a * c
    if discriminant >= 0:
        root = [(-b + isqrt(discriminant)) // (2 * a), (-b - int(isqrt(discriminant))) // (2 * a)]
        root = list(filter(lambda p: n[0] % p == 0, root))
        if len(root) > 0:
            n = n[0]
            p = abs(root[0])
            q = n // p
            e = 65537
            r = (p - 1) * (q - 1)
            d = inverse(e, r)
            m = pow(cipher, d, n)
            print(long_to_bytes(m))
            exit()


for i in range(1, 100):
    solve(n, [x[0], x[1] + i * x[0]])

for i in range(1, 100):
    solve(n, [x[0] + i * x[1], x[1]])