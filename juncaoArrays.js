let a = [1, 2, 3, 4, 5]
let b = [10, 11, 12, 13]
a = [...a, ...b]

a.forEach(result => {
    console.log(result)
})