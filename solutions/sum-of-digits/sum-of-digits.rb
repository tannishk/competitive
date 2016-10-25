def total(a)
	if(a == 0)
		return 0
	else
		return (a % 10 ) + total(a / 10)
	end
end

t = gets.chomp.to_i
while(t>0)
	n = gets.chomp.to_i
	puts total(n)
	t -= 1
end
