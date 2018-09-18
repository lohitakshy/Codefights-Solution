Construct an array b of prefix sums of the given array a.

b is defined as:

  b[0]   = a[0]
  b[1]   = a[0] + a[1]
  b[2]   = a[0] + a[1] + a[2]
  ...
  b[n - 1] = a[0] + a[1] + ... + a[n - 1]
where n is the length of a.

Example

For a = [1, 2, 3], the output should be
prefixSums(a) = [1, 3, 6].

b would be equal to [1, 1 + 2, 1 + 2 + 3] = [1, 3, 6]
