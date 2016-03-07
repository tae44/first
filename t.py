# -*- coding: utf-8 -*-

c(a,b)
[c] + merge(mro(a),mro(b),[a,b])
[c] + merge([a,o],[b,o],[a,b])
[c,a] + merge([o],[b,o],[b])
[c,a,b] + merge([o],[o])
[c,a,b,o]

c(b,a)
[c] + merge(mro(b),mro(a),[b,a])
[c] + merge([b,o],[a,o],[b,a])
[c,b] + merge([o],[a,o],[a])
[c,b,a] + merge([o],[o])
[c,b,a,o]

c(a,b) + b(a)
[c] + merge(mro(a),mro(b),[a,b])
[c] + merge([a,o],([b]+merge(mro(a),[a])),[a,b])
[c] + merge([a,o],([b]+merge([a,o],[a]),[a,b]))
[c] + merge([a,o],([b,a]+merge([o])),[a,b])
[c] + merge([a,o],[b,a,o],[a,b])

c(b,a) + b(a)
[c] + merge(mro(b),mro(a),[b,a])
[c] + merge([a,o],([b]+merge(mro(a),[a])),[b,a])
[c] + merge([a,o],([b]+merge([a,o],[a])),[b,a])
[c] + merge([a,o],([b,a]+merge([o])),[b,a])
[c] + merge([a,o],[b,a,o],[b,a])
[c,b] + merege([a,o],[a,o],[a])
[c,b,a] + merge([o],[o])
[c,b,a,o]

