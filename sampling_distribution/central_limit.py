# Demonstration of central limit theorem
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import numpy as np
from matplotlib import pyplot as plt
import tensorflow as tf
import tensorflow_probability as tfp


def sample_mean_distribution(dist, sample_size, nr_sample):
    ret = []
    for idx in range(nr_sample):
        sample = dist.sample(sample_size)
        ret.append(np.mean(sample))
    return np.array(ret)

def simulate_central_limit():
    poisson = tfp.distributions.Poisson(rate=1.0)
    poisson_sample = poisson.sample(10000)
    plt.hist(poisson_sample, bins = 100)
    plt.show()
    samples = sample_mean_distribution(poisson, 25, 10000)
    plt.hist(samples, bins = 100)
    plt.show()


if __name__ == "__main__":
    simulate_central_limit()
