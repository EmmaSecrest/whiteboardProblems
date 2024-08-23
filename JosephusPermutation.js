function josephusSurvivor(n, k) {
  let array = Array.from({ length: n }, (_, index) => index + 1);
  let ix = 0;
  let killedComponents = [];

  while (array.length > 1) {
    ix = (ix + k - 1) % array.length;
    let numberRemoved = array.splice(ix, 1)[0];
    killedComponents.push(numberRemoved);
  }

  return array[0];
}

console.log(josephusSurvivor(7, 3));
