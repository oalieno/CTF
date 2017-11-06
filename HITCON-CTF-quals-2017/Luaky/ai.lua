function play(x)
    if not _G.i then  _G.i = 0 end
    _G.i = _G.i + 1
    
    -- first stage
    if _G.i <= 100000 then
        return (x + 3) % 3

    -- second stage
    elseif _G.i <= 200000 then
        magic = 1640531527
        limit = 4294967296
        if _G.i % 100000 == 1 then return 0 end
        if _G.i % 100000 == 2 then
            _G.x1 = x
            _G.y1 = 0
            _G.y0 = 0
            _G.ll = 0
            _G.hh = limit - 1
            _G.cc = -1
            _G.pp = -1
            return _G.y0
        end
        if x ~= (_G.x1 + _G.y1 + 2) % 3 then _G.cc = _G.cc + 1 end
        _G.hh = math.min(_G.hh, magic * (_G.i % 100000 - 2) - limit * _G.cc + _G.pp)
        _G.ll = math.max(_G.ll, magic * (_G.i % 100000 - 2) - limit * (_G.cc + 1) + _G.pp)
        _G.pp = _G.pp + _G.y1

        e = 0
        m = (_G.ll + _G.hh) / 2
        m = (m - magic * (_G.i % 100000 - 1) + _G.pp) % limit
        if m - magic + _G.y0 < 0 then e = 1 end
        _G.x1 = x
        _G.y1 = _G.y0
        _G.y0 = (_G.x1 + _G.y1 + e + 2 + 2) % 3
        return _G.y0
        
    -- third stage
    else
        return 0
    end
end
