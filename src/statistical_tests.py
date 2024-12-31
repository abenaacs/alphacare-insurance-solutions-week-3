from scipy.stats import ttest_ind


def t_test_groups(group1, group2, group_name):
    """
    Performs a t-test between two groups.
    """
    t_stat, p_value = ttest_ind(group1, group2)
    print(f"T-statistic for {group_name}: {t_stat}, P-value: {p_value}")
    if p_value < 0.05:
        print(f"Reject the null hypothesis: Significant differences in {group_name}.")
    else:
        print(
            f"Fail to reject the null hypothesis: No significant differences in {group_name}."
        )
