# Awesome Hyperparameter Optimization
We would like to maintain a list of resources about Hyperparameter Optimization. 

We mark work contributed by [Thinklab](http://thinklab.sjtu.edu.cn) with ✨.

*Maintained by members in SJTU-Thinklab: Wei Liu, Shuwan Feng and Junchi Yan.*

We are looking for post-docs interested in machine learning especially for learning combinatorial solvers, dynamic graphs, and reinforcement learning. Please send your up-to-date resume via yanjunchi AT sjtu.edu.cn.

## [Content](#content)

<!-- <tr><td><a href="#survey-papers">1. Survey</a></td></tr>  -->
<table>

<tr>
	<td><a href=#survey>1 Survey</a></td>
</tr>
<tr>
	<td><a href=#classical-optimization-technique>2 Classical Optimization Technique</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#classical-optimization-techniquesimple-search-scheme>2.1 Simple Search Scheme</a></td>
</tr>
<tr>
	<td>&emsp;&emsp;<a href=#classical-optimization-techniquesimple-search-schemegradient-based-search>2.1.1 Gradient-based Search</a></td>
</tr>
<tr>
	<td>&emsp;&emsp;<a href=#classical-optimization-techniquesimple-search-schemegrid-search>2.1.2 Grid Search</a></td>
</tr>
<tr>
	<td>&emsp;&emsp;<a href=#classical-optimization-techniquesimple-search-schemerandom-search>2.1.3 Random Search</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#classical-optimization-techniquebayesian-optimization>2.2 Bayesian Optimization</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#classical-optimization-techniqueheuristic-search>2.3 Heuristic Search</a></td>
</tr>
<tr>
	<td><a href=#acceleration-method>3 Acceleration Method</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#acceleration-methodmulti-fidelity-optimization>3.1 Multi-fidelity Optimization</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#acceleration-methodbandit-based-algorithm>3.2 Bandit-based Algorithm</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#acceleration-methodearly-stop>3.3 Early Stop</a></td>
</tr>
<tr>
	<td><a href=#dynamic-algorithm-configuration>4 Dynamic Algorithm Configuration</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#dynamic-algorithm-configurationgradient-based-optimizer>4.1 Gradient-based Optimizer</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#dynamic-algorithm-configurationpopulation-based-algorithm>4.2 Population-based Algorithm</a></td>
</tr>
<tr>
	<td>&emsp;<a href=#dynamic-algorithm-configurationreinforcement-learning-method>4.3 Reinforcement Learning Method</a></td>
</tr>
<tr>
	<td><a href=#application>5 Application</a></td>
</tr>
</table>




## [Survey](#content)

1. **Algorithms for hyper-parameter optimization** NeurIPS, 2011. [paper](https://proceedings.neurips.cc/paper/2011/file/86e8f7ab32cfd12577bc2619bc635690-Paper.pdf)

    *Bergstra, James and Bardenet, R{\\'e}mi and Bengio, Yoshua and K{\\'e}gl, Bal{\\'a}zs*

2. **Taking the human out of the loop: A review of Bayesian optimization** Proceedings of the IEEE, 2015. [paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7352306&tag=1)

    *Shahriari, Bobak and Swersky, Kevin and Wang, Ziyu and Adams, Ryan P and De Freitas, Nando*

3. **A review of automatic selection methods for machine learning algorithms and hyper-parameter values** Network Modeling Analysis in Health Informatics and Bioinformatics, 2016. [paper](https://link.springer.com/article/10.1007/s13721-016-0125-6)

    *Luo, Gang*

4. **Hyperparameter optimization in learning systems** Journal of Membrane Computing, 2019. [paper](https://link.springer.com/article/10.1007/s41965-019-00023-0)

    *Andonie, R{\\u{a}}zvan*

5. **Hyper-parameter optimization: A review of algorithms and applications** Arxiv, 2020. [paper](https://arxiv.org/pdf/2003.05689.pdf)

    *Yu, Tong and Zhu, Hong*

6. **On hyperparameter optimization of machine learning algorithms: Theory and practice** Neurocomputing, 2020. [paper](https://arxiv.org/pdf/2007.15745.pdf)

    *Yang, Li and Shami, Abdallah*

7. **Methods for Hyperparameters Optimization in Learning Approaches: An Overview** ICML, 2020. [paper](https://link.springer.com/chapter/10.1007/978-3-030-64583-0_11)

    *Del Buono, Nicoletta and Esposito, Flavia and Selicato, Laura*

8. **Automated machine learning: Review of the state-of-the-art and opportunities for healthcare** Artificial intelligence in medicine, 2020. [paper](https://www.sciencedirect.com/science/article/pii/S0933365719310437)

    *Waring, Jonathan and Lindvall, Charlotta and Umeton, Renato*

9. **A survey on hyperparameters optimization algorithms of forecasting models in smart grid** Sustainable Cities and Society, 2020. [paper](https://www.researchgate.net/profile/Nadeem-Javaid/publication/341464056_A_Survey_on_Hyperparameters_Optimization_Algorithms_of_Forecasting_Models_in_Smart_Grid/links/5ec2f1e192851c11a873ffbf/A-Survey-on-Hyperparameters-Optimization-Algorithms-of-Forecasting-Models-in-Smart-Grid.pdf)

    *Khalid, Rabiya and Javaid, Nadeem*

10. **AutoML: A survey of the state-of-the-art** Knowledge-Based Systems, 2021. [paper](https://arxiv.org/pdf/1908.00709.pdf?arxiv.org)

    *He, Xin and Zhao, Kaiyong and Chu, Xiaowen*

11. **Hyperparameter optimization: Foundations, algorithms, best practices and open challenges** Arxiv, 2021. [paper](https://arxiv.org/pdf/2107.05847.pdf)

    *Bischl, Bernd and Binder, Martin and Lang, Michel and Pielok, Tobias and Richter, Jakob and Coors, Stefan and Thomas, Janek and Ullmann, Theresa and Becker, Marc and Boulesteix, Anne-Laure and others*

12. **Survey on Hyperparameter Optimization Using Nature-Inspired Algorithm of Deep Convolution Neural Network** Intelligent and Cloud Computing, 2021. [paper](https://link.springer.com/chapter/10.1007/978-981-15-5971-6_77)

    *Mohakud, Rasmiranjan and Dash, Rajashree*

13. **Hyperparameter Optimization Techniques for Designing Software Sensors Based on Artificial Neural Networks** Sensors, 2021. [paper](https://www.mdpi.com/1424-8220/21/24/8435)

    *Blume, Sebastian and Benedens, Tim and Schramm, Dieter*

14. **Multi-Objective Hyperparameter Optimization--An Overview** Arxiv, 2022. [paper](https://arxiv.org/pdf/2206.07438.pdf)

    *Karl, Florian and Pielok, Tobias and Moosbauer, Julia and Pfisterer, Florian and Coors, Stefan and Binder, Martin and Schneider, Lennart and Thomas, Janek and Richter, Jakob and Lang, Michel and others*

## [Classical Optimization Technique](#content)

### [Classical Optimization Technique/Simple Search Scheme](#content)

### [Classical Optimization Technique/Simple Search Scheme/Gradient-based Search](#content)

1. **Gradient-based optimization of hyperparameters** Neural computation, 2000. [paper](https://www.researchgate.net/profile/Y-Bengio/publication/12368222_Gradient-Based_Optimization_of_Hyperparameters/links/546cd2620cf26e95bc3ca67e/Gradient-Based-Optimization-of-Hyperparameters.pdf)

    *Bengio, Yoshua*

### [Classical Optimization Technique/Simple Search Scheme/Grid Search](#content)

1. **A practical guide to support vector classification** , 2003. [paper](http://www.datascienceassn.org/sites/default/files/Practical%20Guide%20to%20Support%20Vector%20Classification.pdf)

    *Hsu, Chih-Wei and Chang, Chih-Chung and Lin, Chih-Jen and others*

### [Classical Optimization Technique/Simple Search Scheme/Random Search](#content)

1. **Random search for hyper-parameter optimization** Journal of machine learning research, 2012. [paper](https://www.jmlr.org/papers/volume13/bergstra12a/bergstra12a.pdf?source=post_page---------------------------)

    *Bergstra, James and Bengio, Yoshua*

### [Classical Optimization Technique/Bayesian Optimization](#content)

1. **Algorithms for hyper-parameter optimization** NeurIPS, 2011. [paper](https://proceedings.neurips.cc/paper/2011/file/86e8f7ab32cfd12577bc2619bc635690-Paper.pdf)

    *Bergstra, James and Bardenet, R{\\'e}mi and Bengio, Yoshua and K{\\'e}gl, Bal{\\'a}zs*

2. **Freeze-thaw Bayesian optimization** Arxiv, 2014. [paper](https://arxiv.org/pdf/1406.3896.pdf)

    *Swersky, Kevin and Snoek, Jasper and Adams, Ryan Prescott*

3. **Taking the human out of the loop: A review of Bayesian optimization** Proceedings of the IEEE, 2015. [paper](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=7352306&tag=1)

    *Shahriari, Bobak and Swersky, Kevin and Wang, Ziyu and Adams, Ryan P and De Freitas, Nando*

### [Classical Optimization Technique/Heuristic Search](#content)

1. **Survey on Hyperparameter Optimization Using Nature-Inspired Algorithm of Deep Convolution Neural Network** Intelligent and Cloud Computing, 2021. [paper](https://link.springer.com/chapter/10.1007/978-981-15-5971-6_77)

    *Mohakud, Rasmiranjan and Dash, Rajashree*

## [Acceleration Method](#content)

### [Acceleration Method/Multi-fidelity Optimization](#content)

1. **Gaussian process bandit optimisation with multi-fidelity evaluations** NeurIPS, 2016. [paper](https://proceedings.neurips.cc/paper/2016/file/605ff764c617d3cd28dbbdd72be8f9a2-Paper.pdf)

    *Kandasamy, Kirthevasan and Dasarathy, Gautam and Oliva, Junier B and Schneider, Jeff and P{\\'o}czos, Barnab{\\'a}s*

### [Acceleration Method/Bandit-based Algorithm](#content)

1. **Hyperband: A novel bandit-based approach to hyperparameter optimization** JMLR, 2017. [paper](https://www.jmlr.org/papers/volume18/16-558/16-558.pdf)

    *Li, Lisha and Jamieson, Kevin and DeSalvo, Giulia and Rostamizadeh, Afshin and Talwalkar, Ameet*

### [Acceleration Method/Early Stop](#content)

1. **Freeze-thaw Bayesian optimization** Arxiv, 2014. [paper](https://arxiv.org/pdf/1406.3896.pdf)

    *Swersky, Kevin and Snoek, Jasper and Adams, Ryan Prescott*

## [Dynamic Algorithm Configuration](#content)

### [Dynamic Algorithm Configuration/Gradient-based Optimizer](#content)

1. **Online learning rate adaptation with hypergradient descent** ICLR, 2018. [paper](https://arxiv.org/pdf/1703.04782.pdf)

    *Baydin, Atilim Gunes and Cornish, Robert and Rubio, David Martinez and Schmidt, Mark and Wood, Frank*

### [Dynamic Algorithm Configuration/Population-based Algorithm](#content)

1. **Population based training of neural networks** Arxiv, 2017. [paper](https://arxiv.org/pdf/1711.09846.pdf?source=post_page---------------------------)

    *Jaderberg, Max and Dalibard, Valentin and Osindero, Simon and Czarnecki, Wojciech M and Donahue, Jeff and Razavi, Ali and Vinyals, Oriol and Green, Tim and Dunning, Iain and Simonyan, Karen and others*

### [Dynamic Algorithm Configuration/Reinforcement Learning Method](#content)

1. **Fast efficient hyperparameter tuning for policy gradient methods** NeurIPS, 2019. [paper](https://proceedings.neurips.cc/paper/2019/file/743c41a921516b04afde48bb48e28ce6-Paper.pdf)

    *Paul, Supratik and Kurin, Vitaly and Whiteson, Shimon*

## [Application](#content)

1. **A survey on hyperparameters optimization algorithms of forecasting models in smart grid** Sustainable Cities and Society, 2020. [paper](https://www.researchgate.net/profile/Nadeem-Javaid/publication/341464056_A_Survey_on_Hyperparameters_Optimization_Algorithms_of_Forecasting_Models_in_Smart_Grid/links/5ec2f1e192851c11a873ffbf/A-Survey-on-Hyperparameters-Optimization-Algorithms-of-Forecasting-Models-in-Smart-Grid.pdf)

    *Khalid, Rabiya and Javaid, Nadeem*

2. **Evaluation of hyperparameter optimization in machine and deep learning methods for decoding imagined speech EEG** Sensors, 2020. [paper](https://www.mdpi.com/1424-8220/20/16/4629)

    *Cooney, Ciaran and Korik, Attila and Folli, Raffaella and Coyle, Damien*

3. **Hyperparameter Optimization Techniques for Designing Software Sensors Based on Artificial Neural Networks** Sensors, 2021. [paper](https://www.mdpi.com/1424-8220/21/24/8435)

    *Blume, Sebastian and Benedens, Tim and Schramm, Dieter*

