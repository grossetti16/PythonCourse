    # -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 01:29:56 2020

@author: Asus
"""
import pandas as pd 
import pystan

data = pd.read_csv("trend2.csv")
data= data.dropna() # rid of NaN's
data.columns = data.columns.map (str.strip)
data.country = data.country.str.strip() #lookup 
datactr = data.country.unique()
countries = len(datactr)
countrylu = dict(zip(datactr, range(len(datactr))))
country = data['cc'] = data.country.replace(countrylu).values

gini_net = data.gini_net.values
rgdpl =data.rgdpl.values
church2 = data.church2.values

data_1 = {'z': len(church2),
           'p': countries,
           'country':country+1,
           'e': gini_net,
           'g': rgdpl,
           'y':church2
}

model_1 = '''
data {

  int<lower=0> p; 
  int<lower=0> z; 
  int<lower=1,upper=p> country[z];
  vector[z] e;
  vector[z] g;
  vector[z] y;

} 

parameters {

  vector[p] a;
  vector[2] b;
  real mu_a;
  real<lower=0,upper=100> sigma_a;
  real<lower=0,upper=100> sigma_y;

} 

transformed parameters {

  vector[z] m;
  vector[z] y_hat;
  for (i in 1:z) {
   m[i] = a[country[i]] + g[i] * b[1];
   y_hat[i] = m[i] + e[i] * b[2];
    }

}

model {

  sigma_y ~ uniform(0, 100);
  sigma_a ~ uniform(0, 100);
  mu_a ~ normal(0, 10);
  a ~ normal(mu_a, sigma_a);
  b ~ normal(0, 10);
  y ~ normal(y_hat, sigma_y);

}
'''
modelfit = pystan.stan(model_code = model_1, data = data_1, iter=1000, chains=2)
print(modelfit)



#I had difficulties running STAN with the error "Unable to find vcvarsall.bat",after lookingand trying
#for solutions I was not able to get it to run. I understand you told us to speak with you about it ahead of time,
#but I started late with this homework and was not able to get back to you about this issue and I apologize for this situation
#I have left the STAN code above.

