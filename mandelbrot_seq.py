import numpy as np
import cmath
import matplotlib.pyplot as plt
import time

def prompt_parts():
  cr = float(input("Real part > ") or -.5)
  ci = float(input("Imag part > ") or .5)

  c = cr + ci * 1j  # Can use complex(cr,ci)

  return c

def escape_steps(c, iters=80, get_seq=False):

  # TODO more rigorous test of boundedness? Some numbers clearly diverge to inf
  # (any real > 0) yet they will only be picked up after sufficient iters
  #iters = 80  # Optional parameter
  
  #seq = [None for _ in range(iters)]
  #
  #seq[0] = 0
  seq = [0]
  escaped = False
  
  # TODO test out how much increasing iters affects computation time
  # TODO seq is only needed if get_seq=True, else just count.
  # ^Actually seq is useful to check repeats for faster determination of some
  # point in set---but this is probably a small subset.
  # TODO print to file for plotting high res (avoid core dump?)
  # autoname file based on center, radius, res, maxiter
  # TODO quickly determine if certain points are bounded? Or certain points
  # clearly unbounded after anough iters?
  for i in range(1, iters):
    #seq[i] = seq[i-1]**2 + c
    seq.append(seq[i-1]**2 + c)
    if cmath.polar(seq[i])[0] > 2:  # Magnitude > 2
      escaped = True
      break

  if get_seq:           # return seq if desired
    return seq
  if escaped:           # return steps taken to escape
    return i
  #return iters + 1      # return something to indicate that z_n did not escape
  return 0              # Did not escape

def v_escape_steps(c, iters=80): # Vectorized version of escape_steps()
  # c should be nparray
  #c = np.array([1+0j,2+0j,-2+0j,-1+0j,1j])
  #print(c)
  steps = np.ones(np.shape(c)) # Grid of steps taken
  # If z_0 = 0, each c takes at least 1 step to escape.
  steps = np.where(np.abs(c)>2, steps, steps + 1)
  # Check where |z_1| > 2
  #print('steps declared')
  c_init = c                    # Grid of starting values
  # c is z_1
  #print('c_init declared')
  for i in range(2, iters):
  #  print(f'begin loop iter = {i}')
    #c = np.multiply(c,c,where=np.abs(c)<2) + c_init
    # ^Not as good because we keep adding c_init anyway, but works now
    #c = np.multiply(c,c) + c_init # Leads to NANs
    steps = np.where(np.abs(c)>2, steps, steps + 1)
    # Should steps be initialized at 1s instead of 0s?
    # i=2: check where |z_1|>2. Then compute z_2.
    c = np.where(np.abs(c)>2, c, c * c + c_init)
    # After first iteration we are at z_2
    # Can't pass c in cmath.polar()
  steps = np.where(np.abs(c)>2, steps, 0)
  # ^Can we check where steps=i instead of abs?
  #  print(c)
  #print('loop exit')
  # XXX multiply where to omit anything outside of 2? missing way to count steps
  return steps

def plot_seq(seq):
  reals = [x.real for x in seq]
  imags = [x.imag for x in seq]
  
  print(seq)
  
  plt.plot(reals,imags,'o-')
  #plt.axis("scaled")
  plt.gca().set_aspect("equal")
  plt.axis([-3,3,-3,3])
  plt.show()

def plot_set():
  center, radius = (0,0), 2.2
  # minibrot
  #center = (-1.86,0)
  #radius = .003
  #center = (.1,.65)
  #radius = .05
  #center = (.13,.61)
  #radius = .02
  xmin, xmax = center[0] - radius, center[0] + radius
  ymin, ymax = center[1] - radius, center[1] + radius
  maxiters = 80
  res = 1001    # Resolution (odd number to include originin, even to omit)
                # Including the origin (and real axis) is meaningful because
                # these numbers are indeed in the Mandelbrot set.
  # Segmentation fault (core dumped) at res=5001, iters=20
  # 2001 runs in <10s, iters=20
  # 3001 runs in 16s, iters=20
  # 4001 runs in >30s, iters=20
  #xin,yin = np.mgrid[-3:3:7j, -3:3:7j]
  x = np.linspace(xmin, xmax, res)
  y = np.linspace(ymin, ymax, res)
  xs, ys = np.meshgrid(x,y,sparse=True)
  #xys = np.meshgrid(x,y,sparse=True)
  vcomplex = np.vectorize(complex) # TODO can we initialize a complex grid?
  # Consider C++ or Fortran
  cs = vcomplex(xs,ys)
  tstart = time.time()
  zs = v_escape_steps(cs, iters=maxiters)#;quit() # XXX
  tstop = time.time()
  print(tstop-tstart)
  #cs = lambda a,b: vcomplex(a,b)
  vescape = np.vectorize(escape_steps)
  tstart = time.time()
  zs = vescape(cs, iters=maxiters)
  tstop = time.time()
  print(tstop-tstart)
  # XXX new vectorized fun isn't faster at res=2001 :(
  #plt.contourf(x,y,zs)
  # TODO change ticks on imshow plot
  # TODO set_bad() for masked values (np.nan or -1?)
  plt.imshow(zs, extent=[xmin,xmax,ymin,ymax],\
             interpolation='antialiased')  # default seems to be 'antialiased'
      #extent=[-zs.shape[1]/2., zs.shape[1]/2., -zs.shape[0]/2., zs.shape[0]/2. ])
      # Centers the labels but still represents number of squares.
  plt.axis("scaled")
  plt.colorbar()
  plt.title(r"Resolution={res}$\times${res}. Max iters={maxiters}".format(res=res, maxiters=maxiters))
  plt.show()
  #zs = np.
  #plt.plot(x,y,'o', color='k')
  #plt.show()

if __name__ == "__main__":
  if 0:
    c = prompt_parts()
    get_seq = True
    seq = escape_steps(c, get_seq=get_seq, iters=80)
    print(seq)
    if get_seq:
      plot_seq(seq)

  else:
    plot_set()




