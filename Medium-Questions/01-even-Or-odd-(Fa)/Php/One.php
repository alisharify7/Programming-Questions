<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>

    <?php
    if (isset($_POST["number"]))
    {
        $number = number_format($_POST["number"]);
        if ($number > 100 && $number < 0)
        {
            exit("Number not between1 to 100");
        }
        if ($number % 2 == 0)
        {
            echo("<h1> Even Number </h1>");
        }
        else
        {
            echo("<h1> Not a Even Number </h1>");
        }
    }


    ?>

    <form action="" method="post">
        <input type="text" name="number" id="number" placeholder="Enter Number Here ">
        <input type="submit" value="submit">
    </form>
</body>
</html>
