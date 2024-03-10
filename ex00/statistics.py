def ft_statistics(*args, **kwargs) -> None:
    """ft_statistics"""
    try:
        if not args:
            for k, v in kwargs.items():
                print('ERROR')
        else:
            assert len(args) != 0, "empty data"
            results = {}
            for k, v in kwargs.items():
                if 'mean' == v:
                    print(f"mean : {ft_mean(args)}")
                if 'median' == v:
                    print(f"median : {ft_median(args)}")
                if 'quartile' == v:
                    print(f"quartile : {ft_quartile(args)}")
                if 'std' == v:
                    print(f"std : {ft_std(args)}")
                if 'var' == v:
                    print(f"var : {ft_var(args)}")
            return results
    except AssertionError as ae:
        print(f'{type(ae).__name__}: {ae}')


def ft_mean(lst):
    """mean"""
    if len(lst) > 0:
        return float(sum(lst)/len(lst))
    return None


def ft_median(lst):
    """median"""
    if len(lst) > 0:
        return percentil(lst, 0.5)
    return None


def ft_quartile(lst):
    """quartile"""
    if len(lst) > 0:
        result = list()
        result.append(percentil(lst, 0.25))
        result.append(percentil(lst, 0.75))
        return result
    else:
        return None


def ft_var(lst):
    """var"""
    if len(lst) > 0:
        mean = ft_mean(lst)
        var = 0.0
        for elem in lst:
            var += (elem - mean) * (elem - mean)
        var = var / len(lst) - 1
        return var
    else:
        return None


def ft_std(lst):
    """std"""
    if len(lst) > 0:
        mean = ft_mean(lst)
        dev = 0.0
        for elem in lst:
            dev += (elem - mean) ** 2
        dev = dev / len(lst)
        dev = dev**(1/2)
        return dev
    else:
        return None


def percentil(lst, pos):
    """percentil"""
    sorted_list = sorted(lst)
    lst = tuple(sorted_list)
    index = float(len(lst) - 1) * pos
    if (index).is_integer():
        return float(lst[int(index)])
    n1 = lst[int(index)]
    n2 = lst[int(index) + 1]
    quart = n1 * (1 - pos) + n2 * pos
    return quart
