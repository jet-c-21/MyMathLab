import math
import scipy


def get_z_score(x, mean, std) -> float:
    return (x - mean) / std


def get_z_star(confidence_level: float):
    return abs(scipy.stats.norm.ppf((1 - confidence_level) * 0.5))


def get_t_star(confidence_level: float, df: int):
    return abs(scipy.stats.t.ppf((1 - confidence_level) * 0.5, df))


def get_confidence_level_by_z(z_star: float):
    return scipy.stats.norm.cdf(z_star) - scipy.stats.norm.cdf(- z_star)


def get_confidence_interval_of_prop_by_z(s_p_n: int, s_n: int, confidence_level: float) -> tuple:
    p_hat = s_p_n / s_n
    std_e_of_sp = math.sqrt((p_hat * (1 - p_hat)) / s_n)
    z_star = get_z_star(confidence_level)
    margin_error = z_star * std_e_of_sp

    lower_bound = p_hat - margin_error
    higher_bound = p_hat + margin_error

    return lower_bound, higher_bound


def get_confidence_interval_of_mean_by_t(s_n, s_mean, s_std, confidence_level: float) -> tuple:
    std_e_of_sm = s_std / math.sqrt(s_n)
    df = s_n - 1
    t_star = get_t_star(confidence_level, df)
    margin_error = t_star * std_e_of_sm

    lower_bound = s_mean - margin_error
    higher_bound = s_mean + margin_error

    return lower_bound, higher_bound


def get_smallest_sample_size_with_fixed_moe_and_cl_by_z_and_prop(moe: float, cl: float, p_hat=0.5):
    z_star = get_z_star(cl)
    return (z_star * math.sqrt(p_hat * (1 - p_hat)) / moe) ** 2


def get_smallest_sample_size_with_fixed_moe_and_cl_by_z_and_pstd(moe: float, cl: float, p_std):
    z_star = get_z_star(cl)
    return (z_star * p_std / moe) ** 2


def get_smallest_sample_size_with_fixed_moe_and_cl_by_t(moe: float, cl: float, s_std, df: int):
    t_star = get_t_star(cl, df)
    return (t_star * s_std / moe) ** 2


def get_z_statistic(p0: float, s_n: int, s_p_n: int) -> float:
    p_hat = s_p_n / s_n
    std = math.sqrt(p0 * (1 - p0) / s_n)
    return get_z_score(p_hat, p0, std)


def get_p_value_by_z(z_statistic: float) -> float:
    if z_statistic >= 0:
        return 1 - scipy.stats.norm.cdf(z_statistic)
    else:
        return scipy.stats.norm.cdf(z_statistic)


def get_t_statistic_of_mean(p_mean, s_mean, s_std, s_n: int) -> float:
    return (s_mean - p_mean) / (s_std / math.sqrt(s_n))


def get_t_statistic_of_slope(p_slope, s_slope, std_error_of_slope) -> float:
    return (s_slope - p_slope) / std_error_of_slope


def get_p_value_by_t(t_statistic: float, df: int) -> float:
    if t_statistic >= 0:
        return 1 - scipy.stats.t.cdf(t_statistic, df)
    else:
        return scipy.stats.t.cdf(t_statistic, df)


def get_p_value_by_f(f_statistic: float, df_n: int, df_d: int) -> float:
    if f_statistic >= 0:
        return 1 - scipy.stats.f.cdf(f_statistic, df_n, df_d)
    else:
        return scipy.stats.f.cdf(f_statistic, df_n, df_d)
