local number = io.read("n")

if (number > 100 or number < 0) then
    print("Invalid number")
    os.exit(1)
end
if (number % 2 == 0) then
    print("even number")
elseif (number % 2 == 1) then
    print("odd number")
end
