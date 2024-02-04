# function to check if equations intersect in range
def findIntersection(eq1, eq2):
	low = 200000000000000	# bottom of range
	high = 400000000000000	# top of range
	
	# if they are parallel, no intersection
	if eq1.m == eq2.m:
		return False
		
	else:
		# setting up variables to put the equations in ax + by + c = 0 form
		a1=eq1.m; b1=-1; c1=eq1.c
		a2=eq2.m; b2=-1; c2=eq2.c
		
		# calculating the coordinates of the intersection
		x = (b1*c2 - b2*c1) /\
			(a1*b2 - a2*b1)
		y = (c1*a2 - c2*a1) /\
			(a1*b2 - a2*b1)
		
		# if the coordinates are within range
		if x >= low and x <= high and y >= low and y <= high:
			# if the intersection is beyond the starting point of each equation
			if ((eq1.vel[0] > 0 and x >= eq1.pos[0]) or (eq1.vel[0] < 0 and x <= eq1.pos[0])) and\
			   ((eq2.vel[0] > 0 and x >= eq2.pos[0]) or (eq2.vel[0] < 0 and x <= eq2.pos[0])):
				# intersection is valid
				return True
		
		#otherwise no intersection
		return False

# structure with variables for position, velocity, gradient, intercept
class Equation:
	def __init__(self, info):
		self.pos, self.vel, self.m, self.c = info

equations = []

with open('testinput.txt', 'r') as inp:
	stone = inp.readline().split("@ ")
	
	# while line isnt "", split by @, get pos/vel from first 2 values
	while stone != ['']:
		poses = stone[0].split(", ")
		velocities = stone[1].split(", ")
		
		pos = (float(poses[0]), float(poses[1]))
		velocity = (float(velocities[0]), float(velocities[1]))
		
		# calculate gradient and intercept of equation
		m = velocity[1] / velocity[0]
		c = -(m * pos[0]) + pos[1]
		
		# add equation to array
		equations.append(Equation((pos, velocity, m, c)))
		
		# read next line
		stone = inp.readline().split("@ ")
	
	# iterate through equations, finding intersections with rest of equations
	total = 0
	for i, e1 in enumerate(equations):
		for e2 in equations[i+1:]:
			print("quation 1:", e1.pos)
			print("quation 2:", e2.pos)
			
			if findIntersection(e1, e2):
				# increment total if intersection is found
				total += 1
	
	print(total)
