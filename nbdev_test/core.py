# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/acf_plotter.ipynb.

# %% auto 0
__all__ = ['plot_acf', 'calc_pacf']

# %% ../nbs/acf_plotter.ipynb 3
def plot_acf(df_in, nlags=10, *args, **kwargs):
    """caclulates and plots auto-correlation function

    calculates the auto-correlation function and plots the results,
    in a matplotlib figure

    Parameters
    ----------
    df_in : input data structure
        input time series, for which the acf will be calculateds
    nlags : int, optional
        amount of lags to perform the calculation on, by default 10
    """
    acf_values = acf(df_in, nlags=nlags, *args, **kwargs)
    plt.stem(acf_values, markerfmt="C0", linefmt="gray")
    plt.show()


# %% ../nbs/acf_plotter.ipynb 5
def calc_pacf(df_in, nlags=10, *args, **kwargs):
    return pacf(df_in, nlags=nlags, *args, **kwargs)
