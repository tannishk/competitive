def cubeRootNR(x)
	guess = 1
	epsilon = 0.01
	$ctr = 1
	while ((guess**3 - x).abs >= epsilon)
		guess = (x/guess**2 + 2*guess)/3
		$ctr += 1
	end
	return guess
end

puts "Enter a number: "
number = gets.to_f
ans = cubeRootNR(number)
puts "Cube root of #{number} is about #{ans}, try #{$ctr} times"