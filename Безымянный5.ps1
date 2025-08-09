$num1 = [double](Read-Host "Введите первое число")
$num2 = [double](Read-Host "Введите второе число")
$op = Read-Host "Выберите операцию (+, -, *)" 

switch ($op) {
    "+" { $result = $num1 + $num2 }
    "-" { $result = $num1 - $num2 }
    "*" { $result = $num1 * $num2 }
    default { $result = "Ошибка: неизвестная операция" }
}

Write-Host "Результат: $result"  