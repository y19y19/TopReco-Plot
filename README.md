# TopReco-Plot

This repo is for evaluating performance of ML models/algorthms on reconstructing ttbar dileptonic events in CMS experiment.

Under your workspace,
```
mkdir Performance/
cd Performance/
git clone <repo>
```
To save top quark kinematics as numpy arrays for performance evaluation, please use ProcessData_Run2.ipynb.

It saves numpy arrays of kinematics in `Performance/arrays`

To evaluate performance by plotting 1D/2D distributions and RMSE/Bias, please use Plots_ttbar_Run2.ipynb.

It saves plots in `Performance/kinematics` and `Performance/rmse`
