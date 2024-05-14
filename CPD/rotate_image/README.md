# Исходный код
``` rust
pub fn rotate(matrix: &mut Vec<Vec<i32>>) {
    let len = matrix.len() - 1;
    let half = (matrix.len() + 1) / 2;

    for row in 0..half {
        for column in row..(len - row) {
            let (a, b, c, d) =
                (
                matrix[row][column],
                matrix[column][len - row],
                matrix[len - row][len - column],
                matrix[len - column][row]
                );

            matrix[row][column] = d;
            matrix[column][len - row] = a;
            matrix[len - row][len - column] = b;
            matrix[len - column][row] = c;
        }
    }
}
```
# Результат работы
<image src="images/result.png" alt="solve">
