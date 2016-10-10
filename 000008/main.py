"""Problem 8.

Usage:
  main.py

Options:
  -h --help     Show this screen.
  --version     Show version.
"""

from docopt import docopt

adjacent_count = 4


def main(args):
    """Main."""
    global adjacent_count

    segments = []

    # Get matrix as single string
    series = get_series()

    # Split on zero
    series = series.split('0')

    # Filter Short
    series = filter(filter_short_items, series)

    # Sort series
    series = sorted(series, key=len)

    # Get adjacent_count digit segments
    for i in series:
        if len(i) is adjacent_count:
            segments.append(i)
        else:
            last_start_pos = len(i) - (adjacent_count - 1)
            segments.append(i[0:adjacent_count])
            for x in xrange(1, last_start_pos):
                segments.append(i[x:x + adjacent_count])

    # Sort and get max
    greatest = max(segments, key=get_product)
    greatest_product = get_product(greatest)

    print 'Answer: {}'.format(greatest_product)


def get_product(e):
    """Get greatest product."""
    multiples = [int(m) for m in e]
    product = reduce(lambda x, y: x * y, multiples)
    return product


def filter_short_items(e):
    """Remove items shorter than adjacent_count."""
    global adjacent_count
    return len(e) >= adjacent_count


def get_series():
    """Get series."""
    return ''.join([
        '73167176531330624919225119674426574742355349194934',
        '96983520312774506326239578318016984801869478851843',
        '85861560789112949495459501737958331952853208805511',
        '12540698747158523863050715693290963295227443043557',
        '66896648950445244523161731856403098711121722383113',
        '62229893423380308135336276614282806444486645238749',
        '30358907296290491560440772390713810515859307960866',
        '70172427121883998797908792274921901699720888093776',
        '65727333001053367881220235421809751254540594752243',
        '52584907711670556013604839586446706324415722155397',
        '53697817977846174064955149290862569321978468622482',
        '83972241375657056057490261407972968652414535100474',
        '82166370484403199890008895243450658541227588666881',
        '16427171479924442928230863465674813919123162824586',
        '17866458359124566529476545682848912883142607690042',
        '24219022671055626321111109370544217506941658960408',
        '07198403850962455444362981230987879927244284909188',
        '84580156166097919133875499200524063689912560717606',
        '05886116467109405077541002256983155200055935729725',
        '71636269561882670428252483600823257530420752963450',
    ])


if __name__ == '__main__':
    args = docopt(__doc__, version='0.0.1')
    main(args)
