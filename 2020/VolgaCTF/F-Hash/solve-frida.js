var base = ptr(Process.enumerateModulesSync()[0].base)
var recursive_func_ptr = base.add(0x13b0)

var mem = {}
Interceptor.attach(recursive_func_ptr, {
    onEnter: function (args) {
        this.buf = args[0]
        this.hash = args[1] + '-' + args[2] + '-' + args[3]
        if (mem[this.hash] !== undefined) {
            args[1] = ptr(1)
        }
    },
    onLeave: function (retval) {
        if (mem[this.hash] === undefined) {
            mem[this.hash] = [this.buf.readU64(), this.buf.add(8).readU64(), this.buf.add(16).readU64()]
        } else {
            this.buf.writeU64(mem[this.hash][0])
            this.buf.add(8).writeU64(mem[this.hash][1])
            this.buf.add(16).writeU64(mem[this.hash][2])
        }
    }
})
