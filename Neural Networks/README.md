# LSTM Model Implementation

- This directory contains model that uses LSTM to predict future prices of forex market
- Data based on GBP/USD, scraped from Bloomberg Terminal

## Development tools

- python
![python](https://res.cloudinary.com/teepublic/image/private/s--TwCcIoc_--/t_Resized%20Artwork/c_fit,g_north_west,h_954,w_954/co_000000,e_outline:48/co_000000,e_outline:inner_fill:48/co_ffffff,e_outline:48/co_ffffff,e_outline:inner_fill:48/co_bbbbbb,e_outline:3:1000/c_mpad,g_center,h_1260,w_1260/b_rgb:eeeeee/c_limit,f_jpg,h_630,q_90,w_630/v1520050660/production/designs/2416585_0.jpg)

- tensorflow
![tensorflow](https://planspace.org/20170318-much_ado_about_the_tensorflow_logo/img/tf-new.jpg)

- keras
![keras](https://keras.io/img/keras-logo-small.jpg)

- scikit-learn
![scikit-learn](https://blogeduonix-2f3a.kxcdn.com/wp-content/uploads/2018/12/Linear-Discriminant-Analysis.jpg)


## Why LSTM rather than RNN?
We have carefully analysed the rationale behind using LSTM for the prediction of forex price. The main reason includes:
- 1. LSTM has memory. So it can memorize the data in the past, making its prediction more reliable.
- 2. LSTM prevents weights from diminishing to zero quickly or exploding.

### contributers

```python
Zhou Zijian
```

```python
Sean Gee
```