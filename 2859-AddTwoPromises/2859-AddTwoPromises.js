// Last updated: 9/3/2025, 11:24:03 AM
/**
 * @param {Promise<number>} promise1
 * @param {Promise<number>} promise2
 * @return {Promise<number>}
 */
var addTwoPromises = async function(promise1, promise2) {
  const [a, b] = await Promise.all([promise1, promise2]);
  return a + b; // async functions return a Promise automatically
};
