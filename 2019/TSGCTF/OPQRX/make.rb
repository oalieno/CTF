require 'securerandom'

def miller_rabin(n)
  raise ArgumentError unless n >= 2
  return true if n == 2
  return false if n == 1 or n.even?
  return n != 9 if n < 15

  d, r = n-1, 0
  while d.even?
    d >>= 1
    r += 1
  end

  30.times do
    a = rand(2..(n-2))
    x = a.pow(d, n)

    ok = false
    next if x == 1 or x == n-1
    (r-1).times do
      x = (x*x) % n
      if x == n-1
        ok = true
        break
      end
    end

    return false unless ok
  end

  true
end

def getprime(bits)
  loop do
    p = SecureRandom.random_number(1<<bits)
    return p if miller_rabin(p)
  end
end

bits = 4096
P, Q = 2.times.map{getprime(bits)}
puts(P)
puts(Q)

F = IO.binread('flag.txt').unpack("H*")[0].hex
X = P^Q
N = P*Q
puts(X)

raise ArgumentError unless F < N

E = 65537
C = F.pow(E, N)

IO.binwrite('flag.enc', [
  'X = %p' % X,
  'N = %p' % N,
  'E = %p' % E,
  'C = %p' % C,
].join("\n"))
