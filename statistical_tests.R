library(rstatix)
library(ggpubr)
library(lawstat)
library(readxl)
library(writexl)
library(exactRankTests)
library(moments)

# Leukemia (ALLAML)
#k acc. cov.
#1 0.917 1.000
#2 0.847 1.000
#3 0.889 1.000
#5 0.847 1.000


amlall_comparison_accuracy <- 
  data.frame(
    knn_k_1 = 0.917,
    knn_k_2 = 0.847,
    knn_k_3 = 0.889,
    knn_k_5 = 0.847,
    rf = 0.972
  )

comparison_coverage <- 
  data.frame(
    knn_k_1 = 1.0,
    knn_k_2 = 1.0,
    knn_k_3 = 1.0,
    knn_k_5 = 1.0,
    rf = 1.0
  )

#k acc. cov.
#1 0.839 1.000
#2 0.839 1.000
#3 0.839 1.000
#5 0.806 1.000
#Random Forest 0.806 1.000


colon_comparison <- 
data.frame(
  knn_k_1 = 0.839,
  knn_k_2 = 0.839,
  knn_k_3 = 0.839,
  knn_k_5 = 0.806,
  rf = 0.806
)


#k acc. cov.
#1 0.956 1.000
#2 0.960 1.000
#3 0.968 1.000
#5 0.960 1.000
#Random Forest 0.996 1.000

ovarian_comparison <-
  data.frame(
    knn_k_1 = 0.956,
    knn_k_2 = 0.960,
    knn_k_3 = 0.968,
    knn_k_5 = 0.960,
    rf = 0.996
  )

#k acc. cov.
#1 0.872 1.000
#2 0.894 1.000
#3 0.851 1.000
#5 0.851 1.000
#Random Forest 0.936 1.000

dlbcl_comparison <- 
  data.frame(
    knn_k_1 = 0.872,
    knn_k_2 = 0.894,
    knn_k_3 = 0.851,
    knn_k_5 = 0.851,
    rf = 0.936
  )

#k acc. cov.
#1 0.801 1.000
#2 0.801 1.000
#3 0.801 1.000
#5 0.787 1.000
#Random Forest 0.949 1.000

prostate_comparison <-
  data.frame(
    knn_k_1 = 0.801,
    knn_k_2 = 0.801,
    knn_k_3 = 0.801,
    knn_k_5 = 0.787,
    rf = 0.949
  )

# Please remember to set working directory
# setwd("")

amlall = read_excel("RESULTS_AML_ALL_final_v3.xlsx_aggs.xlsx")

amlall_A1_k_1 <- filter(amlall, aggregation == "A1" & k == '[1]')

amlall_A1_k_2 <- filter(amlall, aggregation == "A1" & k == '[2]')

amlall_A1_k_1_2 <- filter(amlall, aggregation == "A1" & k == '[1, 2]')

amlall_A2_K_1_2 <- filter(amlall, aggregation == "A2" & k == '[1, 2]')

amlall_A5_k_1_2 <- filter(amlall, aggregation == 'A5' & k == '[1, 2]')

amlall_A7_k_1_2 <- filter(amlall, aggregation == 'A7' & k == '[1, 2]')

amlall_A10_k_1_2 <- filter(amlall, aggregation == "A10" & k == '[1, 2]')


colon = read_excel("RESULTS_COLON_final_v3.xlsx_aggs.xlsx")

colon_A1_k_1 <- filter(colon, aggregation == "A1" & k == '[1]')

colon_A1_k_2 <- filter(colon, aggregation == "A1" & k == '[2]')

colon_A1_k_1_2 <- filter(colon, aggregation == "A1" & k == '[1, 2]')

colon_A10_k_2 <- filter(colon, aggregation == "A10" & k == '[2]')

colon_A10_k_1_2 <- filter(colon, aggregation == "A10" & k == '[1, 2]')

colon_A2_k_1_2 <- filter(colon, aggregation == "A2" & k == '[1, 2]')

colon_A5_k_2 <- filter(colon, aggregation == "A5" & k == '[2]')

colon_A6_k_2 <- filter(colon, aggregation == "A6" & k == '[2]')

colon_A7_k_1_2 <- filter(colon, aggregation == "A7" & k == '[1, 2]')

# ovarian
ovarian = read_excel("RESULTS_ovarian_final_v3.xlsx_aggs.xlsx")
ovarian_A1_k_1 = filter(ovarian, aggregation == "A1" & k == '[1]')
ovarian_A1_k_2 = filter(ovarian, aggregation == "A1" & k == '[2]')
ovarian_A1_k_1_2 <- filter(ovarian, aggregation == "A1" & k == '[1, 2]')

ovarian_A10_k_1 = filter(ovarian, aggregation == "A10" & k == '[1]')
ovarian_A10_k_2 <- filter(ovarian, aggregation == "A10" & k == '[2]')
ovarian_A10_k_1_2 <- filter(ovarian, aggregation == "A10" & k == '[1, 2]')

ovarian_A2_k_1_2 <- filter(ovarian, aggregation == "A2" & k == '[1, 2]')

ovarian_A5_k_1 <- filter(ovarian, aggregation == "A5" & k == '[1]')
ovarian_A5_k_2 <- filter(ovarian, aggregation == "A5" & k == '[2]')
ovarian_A5_k_1_2 <- filter(ovarian, aggregation == "A5" & k == '[1, 2]')

ovarian_A6_k_1 <- filter(ovarian, aggregation == "A6" & k == '[1]')
ovarian_A6_k_2 <- filter(ovarian, aggregation == "A6" & k == '[2]')
ovarian_A6_k_1_2 <- filter(ovarian, aggregation == "A6" & k == '[1, 2]')

ovarian_A7_k_1_2 <- filter(ovarian, aggregation == "A7" & k == '[1, 2]')

dlbcl = read_excel("RESULTS_DLBCL_final_v3.xlsx_aggs.xlsx")
dlbcl_A1_k_1_2 <- filter(dlbcl, aggregation == "A1" & k == '[1, 2]')
dlbcl_A2_k_1_2 <- filter(dlbcl, aggregation == "A2" & k == '[1, 2]')
dlbcl_A7_k_1_2 <- filter(dlbcl, aggregation == "A7" & k == '[1, 2]')


prostate = read_excel("RESULTS_prostate_final_v3.xlsx_aggs.xlsx")
prostate_A1_k_1_2 <- filter(prostate, aggregation == "A1" & k == '[1, 2]')
prostate_A1_k_1 <- filter(prostate, aggregation == "A1" & k == '[1]')
prostate_A1_k_2 <- filter(prostate, aggregation == "A1" & k == '[2]')

prostate_A2_k_1_2 <- filter(prostate, aggregation == "A2" & k == '[1, 2]')

prostate_A5_k_2 <- filter(prostate, aggregation == "A5" & k == '[2]')

prostate_A7_k_1_2 <- filter(prostate, aggregation == "A7" & k == '[1, 2]')

prostate_A10_k_2 <- filter(prostate, aggregation == "A10" & k == '[2]')

accuracy_shapiro_wilk <- data.frame(
   series = 'foo',
   W = 0,
   p = 0
)

accuracy_mgg <- data.frame(
  series = 'foo',
  statistic = 0,
  p = 0
)

wilcoxon_exact <- data.frame(
  series = 'foo',
  V = 0,
  p = 0
)

t_test <- data.frame(
  series = 'foo',
  statistic = 0,
  p = 0
)



apply_all_tests <- function(series, name, comparison, feature) {
  print(name)
  print(feature)
  
  print(summary(series[[feature]]))
  hist(series[[feature]], main = paste("Histogram of" , name))
  
  
  shapiro_result = shapiro.test(series[[feature]])
  print(shapiro_result)
  
  if (feature == 'accuracy') {
    temp <- data.frame(
      series = name,
      W = shapiro_result$statistic,
      p = shapiro_result$p.value
    )
    temp2 <- rbind(accuracy_shapiro_wilk, temp)
    print(temp)
    accuracy_shapiro_wilk <- temp2
    print(accuracy_shapiro_wilk)
    assign('accuracy_shapiro_wilk', accuracy_shapiro_wilk, envir=.GlobalEnv)
  }
  
  
  if (shapiro_result$p.value > 0.05) {
    print(paste(shapiro_result$p.value,' is greater than 0.05 so data is normally distributed.'))
    outliers = series %>% identify_outliers(feature)
    
    print(outliers)
    
    if (nrow(outliers) > 0) {
      print('There are some outliers in data!')
    }
    
    if (feature == 'accuracy') {
     
      knn_k_1_result = series %>% t_test(accuracy ~ 1, mu = comparison$knn_k_1)
      print(knn_k_1_result)
      
      t_test <- rbind(t_test, data.frame(
        series = paste(name, 'knn k=1'),
        statistic = knn_k_1_result$statistic,
        p = knn_k_1_result$p
      ))
      
      if (knn_k_1_result$p < 0.05) {
        print('The values differ significantly for knn, k=1 ')
      }
      
      
      knn_k_2_result = series %>% t_test(accuracy ~ 1, mu = comparison$knn_k_2)
      print(knn_k_2_result)
      
      t_test <- rbind(t_test, data.frame(
        series = paste(name, 'knn k=2'),
        statistic = knn_k_2_result$statistic,
        p = knn_k_2_result$p
      ))
      
      if (knn_k_2_result$p < 0.05) {
        print('The values differ significantly for knn, k=2')
      }
      
      knn_k_3_result = series %>% t_test(accuracy ~ 1, mu = comparison$knn_k_3)
      print(knn_k_3_result)
      
      t_test <- rbind(t_test, data.frame(
        series = paste(name, 'knn k=3'),
        statistic = knn_k_3_result$statistic,
        p = knn_k_3_result$p
      ))
      
      if (knn_k_3_result$p < 0.05) {
        print('The values differ significantly for knn, k=3')
      }
      
      knn_k_5_result = series %>% t_test(accuracy ~ 1, mu = comparison$knn_k_5)
      print(knn_k_5_result)
      
      t_test <- rbind(t_test, data.frame(
        series = paste(name, 'knn k=5'),
        statistic = knn_k_5_result$statistic,
        p = knn_k_5_result$p
      ))
      
      if (knn_k_5_result$p < 0.05) {
        print('The values differ significantly for knn, k=5')
      }
      
      rf_result = series %>% t_test(accuracy ~ 1, mu = comparison$rf)
      print(rf_result)
      
      t_test <- rbind(t_test, data.frame(
        series = paste(name, 'random forest'),
        statistic = rf_result$statistic,
        p = rf_result$p
      ))
      
      if (rf_result$p < 0.05) {
        print('The values differ significantly for random forest')
      }
      
      assign('t_test', t_test, envir=.GlobalEnv)
      
     
    } else {
      print(t_test(series, coverage ~ 1, mu = comparison$knn_k_1))
      print(t_test(series, coverage ~ 1, mu = comparison$knn_k_2))
      print(t_test(series, coverage ~ 1, mu = comparison$knn_k_3))
      print(t_test(series, coverage ~ 1, mu = comparison$knn_k_5))
      print(t_test(series, coverage ~ 1, mu = comparison$rf))
      
      if (t_test(series, coverage ~ 1, mu = comparison$knn_k_1)$p < 0.05) {
        print('The values are statistically significant')
      } else {
        print('The values are not statistically significant')
      }
    }
    
    
  } else {
    print('Data is not normally distributed, p-value is lower that 0.05')
    
    symmetry_results = symmetry.test(series[[feature]], side='both', boot=FALSE)
    print(symmetry_results)
    
    if (feature == 'accuracy') {
      temp <- data.frame(
        series = name,
        statistic = symmetry_results$statistic,
        p = symmetry_results$p.value
      )
      temp2 <- rbind(accuracy_mgg, temp)
      print(temp)
      accuracy_mgg <- temp2
      print(accuracy_mgg)
      assign('accuracy_mgg', accuracy_mgg, envir=.GlobalEnv)
    }
    
    
    print('skewness ')
    print(skewness(series[[feature]]))
    
    if (symmetry_results$p.value > 0.05) {
      
      knn_k_1_result = wilcox.exact(series[[feature]], mu = comparison$knn_k_1, paired = FALSE, alternative = "two.sided", conf.level = 0.95)
      print(knn_k_1_result)
      
      wilcoxon_exact <- rbind(wilcoxon_exact, data.frame(
        series = paste(name, 'knn k=1'),
        V = knn_k_1_result$statistic,
        p = knn_k_1_result$p.value
      ))
      
      if (knn_k_1_result$p.value < 0.05) {
        print('The values differ significantly for knn, k=1 ')
      }
      
      knn_k_2_result = wilcox.exact(series[[feature]], mu = comparison$knn_k_2, paired = FALSE, alternative = "two.sided", conf.level = 0.95)
      print(knn_k_2_result)
      
      wilcoxon_exact <- rbind(wilcoxon_exact, data.frame(
        series = paste(name, 'knn k=2'),
        V = knn_k_2_result$statistic,
        p = knn_k_2_result$p.value
      ))
      
      if (knn_k_2_result$p.value < 0.05) {
        print('The values differ significantly for knn, k=2')
      }
      
      knn_k_3_result = wilcox.exact(series[[feature]], mu = comparison$knn_k_3, paired = FALSE, alternative = "two.sided", conf.level = 0.95)
      print(knn_k_3_result)
      
      wilcoxon_exact <- rbind(wilcoxon_exact, data.frame(
        series = paste(name, 'knn k=3'),
        V = knn_k_3_result$statistic,
        p = knn_k_3_result$p.value
      ))
      
      if (knn_k_3_result$p.value < 0.05) {
        print('The values differ significantly for knn, k=3')
      }
      
      knn_k_5_result = wilcox.exact(series[[feature]], mu = comparison$knn_k_5, paired = FALSE, alternative = "two.sided", conf.level = 0.95)
      print(knn_k_5_result)
      
      wilcoxon_exact <- rbind(wilcoxon_exact, data.frame(
        series = paste(name, 'knn k=5'),
        V = knn_k_5_result$statistic,
        p = knn_k_5_result$p.value
      ))
      
      if (knn_k_5_result$p.value < 0.05) {
        print('The values differ significantly for knn, k=5')
      }
      
      rf_result = wilcox.exact(series[[feature]], mu = comparison$rf, paired = FALSE, alternative = "two.sided", conf.level = 0.95)
      print(rf_result)
      
      wilcoxon_exact <- rbind(wilcoxon_exact, data.frame(
        series = paste(name, 'random forest'),
        V = rf_result$statistic,
        p = rf_result$p.value
      ))
      
      if (rf_result$p.value < 0.05) {
        print('The values differ significantly for random forest')
      }
      
      assign('wilcoxon_exact', wilcoxon_exact, envir=.GlobalEnv)
      
    } 
    else {
      print('The series distribution is not symmetrical, can not perform Wilcoxon Signed Rank Tests')
    }
    ggqqplot(series, x=feature)
    
    
    
    
  }
  
}

apply_all_tests(amlall_A1_k_1, 'AML ALL A1 k=[1]', amlall_comparison_accuracy, 'accuracy')
apply_all_tests(amlall_A1_k_1, 'AML ALL A1 k=[1]', comparison_coverage, 'coverage')

apply_all_tests(amlall_A1_k_2, 'AML ALL A1 k=[2]', amlall_comparison_accuracy, 'accuracy')
apply_all_tests(amlall_A1_k_2, 'AML ALL A1 k=[2]', comparison_coverage, 'coverage')

apply_all_tests(amlall_A1_k_1_2, 'AML ALL A1 k=[1, 2]', amlall_comparison_accuracy, 'accuracy')
apply_all_tests(amlall_A1_k_1_2, 'AML ALL A1 k=[1, 2]', comparison_coverage, 'coverage')

apply_all_tests(amlall_A2_K_1_2, 'AML ALL A2 k=[1, 2]', amlall_comparison_accuracy, 'accuracy')
apply_all_tests(amlall_A2_K_1_2, 'AML ALL A2 k=[1, 2]', comparison_coverage, 'coverage')

apply_all_tests(amlall_A5_k_1_2, 'AML ALL A5 k=[1, 2]', amlall_comparison_accuracy, 'accuracy')
apply_all_tests(amlall_A5_k_1_2, 'AML ALL A5 k=[1, 2]', comparison_coverage, 'coverage')

apply_all_tests(amlall_A7_k_1_2, 'AML ALL A7 k=[1, 2]', amlall_comparison_accuracy, 'accuracy')
apply_all_tests(amlall_A7_k_1_2, 'AML ALL A7 k=[1, 2]', comparison_coverage, 'coverage')

apply_all_tests(amlall_A10_k_1_2, 'AML ALL A10 k=[1, 2]', amlall_comparison_accuracy, 'accuracy')
apply_all_tests(amlall_A10_k_1_2, 'AML ALL A10 k=[1, 2]', comparison_coverage, 'coverage')


# colon
apply_all_tests(colon_A1_k_1, 'COLON A1 k=[1]', colon_comparison, 'accuracy')
apply_all_tests(colon_A1_k_1, 'COLON A1 k=[1]', comparison_coverage, 'coverage')
apply_all_tests(colon_A1_k_2, 'COLON A1 k=[2]', colon_comparison, 'accuracy')
apply_all_tests(colon_A1_k_2, 'COLON A1 k=[2]', comparison_coverage, 'coverage')
apply_all_tests(colon_A1_k_1_2, 'COLON A1 k=[1, 2]', colon_comparison, 'accuracy')
apply_all_tests(colon_A1_k_1_2, 'COLON A1 k=[1, 2]', comparison_coverage, 'coverage')

apply_all_tests(colon_A10_k_2, 'COLON A10 k=[2]', colon_comparison, 'accuracy')
apply_all_tests(colon_A10_k_2, 'COLON A10 k=[2]', comparison_coverage, 'coverage')
apply_all_tests(colon_A10_k_1_2, 'COLON A10 k=[1, 2]', colon_comparison, 'accuracy')
apply_all_tests(colon_A10_k_1_2, 'COLON A10 k=[1, 2]', comparison_coverage, 'coverage')

apply_all_tests(colon_A2_k_1_2, 'COLON A2 k=[1, 2]', colon_comparison, 'accuracy')
apply_all_tests(colon_A2_k_1_2, 'COLON A2 k=[1, 2]', comparison_coverage, 'coverage')
apply_all_tests(colon_A5_k_2, 'COLON A5 k=[2]', colon_comparison, 'accuracy')
apply_all_tests(colon_A5_k_2, 'COLON A5 k=[2]', comparison_coverage, 'coverage')
apply_all_tests(colon_A6_k_2, 'COLON A6 k=[2]', colon_comparison, 'accuracy')
apply_all_tests(colon_A6_k_2, 'COLON A6 k=[2]', comparison_coverage, 'coverage')
apply_all_tests(colon_A7_k_1_2, 'COLON A7 k=[1, 2]', colon_comparison, 'accuracy')
apply_all_tests(colon_A7_k_1_2, 'COLON A7 k=[1, 2]', comparison_coverage, 'coverage')

# ovarian
apply_all_tests(ovarian_A1_k_1, 'OVARIAN A1 k=[1]', ovarian_comparison, 'accuracy')
apply_all_tests(ovarian_A1_k_1, 'OVARIAN A1 k=[1]', comparison_coverage, 'coverage')

apply_all_tests(ovarian_A1_k_2, 'OVARIAN A1 k=[2]', ovarian_comparison, 'accuracy')
apply_all_tests(ovarian_A1_k_2, 'OVARIAN A1 k=[2]', comparison_coverage, 'coverage')

apply_all_tests(ovarian_A1_k_1_2, 'OVARIAN A1 k=[1, 2]', ovarian_comparison, 'accuracy')
apply_all_tests(ovarian_A1_k_1_2, 'OVARIAN A1 k=[1, 2]', comparison_coverage, 'coverage')

apply_all_tests(ovarian_A10_k_1, 'OVARIAN A10 k=[1]', ovarian_comparison, 'accuracy')
apply_all_tests(ovarian_A10_k_1, 'OVARIAN A10 k=[1]', comparison_coverage, 'coverage')
apply_all_tests(ovarian_A10_k_2, 'OVARIAN A10 k=[2]', ovarian_comparison, 'accuracy')
apply_all_tests(ovarian_A10_k_2, 'OVARIAN A10 k=[2]', comparison_coverage, 'coverage')
apply_all_tests(ovarian_A10_k_1_2, 'OVARIAN A10 k=[1, 2]', ovarian_comparison, 'accuracy')
apply_all_tests(ovarian_A10_k_1_2, 'OVARIAN A10 k=[1, 2]', comparison_coverage, 'coverage')

apply_all_tests(ovarian_A2_k_1_2, 'OVARIAN A2 k=[1, 2]', ovarian_comparison, 'accuracy')
apply_all_tests(ovarian_A2_k_1_2, 'OVARIAN A2 k=[1, 2]', comparison_coverage, 'coverage')

apply_all_tests(ovarian_A5_k_1, 'OVARIAN A5 k=[1]', ovarian_comparison, 'accuracy')
apply_all_tests(ovarian_A5_k_1, 'OVARIAN A5 k=[1]', comparison_coverage, 'coverage')

apply_all_tests(ovarian_A5_k_2, 'OVARIAN A5 k=[2]', ovarian_comparison, 'accuracy')
apply_all_tests(ovarian_A5_k_2, 'OVARIAN A5 k=[2]', comparison_coverage, 'coverage')

apply_all_tests(ovarian_A5_k_1_2, 'OVARIAN A5 k=[1, 2]', ovarian_comparison, 'accuracy')
apply_all_tests(ovarian_A5_k_1_2, 'OVARIAN A5 k=[1, 2]', comparison_coverage, 'coverage')

apply_all_tests(ovarian_A6_k_1, 'OVARIAN A6 k=[1]', ovarian_comparison, 'accuracy')
apply_all_tests(ovarian_A6_k_1, 'OVARIAN A6 k=[1]', comparison_coverage, 'coverage')

apply_all_tests(ovarian_A6_k_2, 'OVARIAN A6 k=[2]', ovarian_comparison, 'accuracy')
apply_all_tests(ovarian_A6_k_2, 'OVARIAN A6 k=[2]', comparison_coverage, 'coverage')

apply_all_tests(ovarian_A6_k_1_2, 'OVARIAN A6 k=[1, 2]', ovarian_comparison, 'accuracy')
apply_all_tests(ovarian_A6_k_1_2, 'OVARIAN A6 k=[1, 2]', comparison_coverage, 'coverage')

apply_all_tests(ovarian_A7_k_1_2, 'OVARIAN A7 k=[1, 2]v', ovarian_comparison, 'accuracy')
apply_all_tests(ovarian_A7_k_1_2, 'OVARIAN A7 k=[1, 2]v', comparison_coverage, 'coverage')

# dlbcl

apply_all_tests(dlbcl_A1_k_1_2, 'DLBCL A1 k=[1, 2]', dlbcl_comparison, 'accuracy')
apply_all_tests(dlbcl_A1_k_1_2, 'DLBCL A1 k=[1, 2]', comparison_coverage, 'coverage')

apply_all_tests(dlbcl_A2_k_1_2, 'DLBCL A2 k=[1, 2]', dlbcl_comparison, 'accuracy')
apply_all_tests(dlbcl_A2_k_1_2, 'DLBCL A2 k=[1, 2]', comparison_coverage, 'coverage')

apply_all_tests(dlbcl_A7_k_1_2, 'DLBCL A7 k=[1, 2]', dlbcl_comparison, 'accuracy')
apply_all_tests(dlbcl_A7_k_1_2, 'DLBCL A7 k=[1, 2]', comparison_coverage, 'coverage')

# prostate

apply_all_tests(prostate_A1_k_1_2, 'prostate A1 k=[1, 2]', prostate_comparison, 'accuracy')
apply_all_tests(prostate_A1_k_1_2, 'prostate A1 k=[1, 2]', comparison_coverage, 'coverage')

apply_all_tests(prostate_A1_k_1, 'prostate A1 k=[1]', prostate_comparison, 'accuracy')
apply_all_tests(prostate_A1_k_1, 'prostate A1 k=[1]', comparison_coverage, 'coverage')

apply_all_tests(prostate_A1_k_2, 'prostate A1 k=[2]', prostate_comparison, 'accuracy')
apply_all_tests(prostate_A1_k_2, 'prostate A1 k=[2]', comparison_coverage, 'coverage')


apply_all_tests(prostate_A2_k_1_2, 'prostate A2 k=[1, 2]', prostate_comparison, 'accuracy')
apply_all_tests(prostate_A2_k_1_2, 'prostate A2 k=[1, 2]', comparison_coverage, 'coverage')

apply_all_tests(prostate_A5_k_2, 'prostate A5 k=[2]', prostate_comparison, 'accuracy')
apply_all_tests(prostate_A5_k_2, 'prostate A5 k=[2]', comparison_coverage, 'coverage')

apply_all_tests(prostate_A7_k_1_2, 'prostate A7 k=[1, 2]', prostate_comparison, 'accuracy')
apply_all_tests(prostate_A7_k_1_2, 'prostate A7 k=[1, 2]', comparison_coverage, 'coverage')

apply_all_tests(prostate_A10_k_2, 'prostate A10 k=[2]', prostate_comparison, 'accuracy')
apply_all_tests(prostate_A7_k_1_2, 'prostate A7 k=[1, 2]', comparison_coverage, 'coverage')



write_xlsx(accuracy_shapiro_wilk, "shapiro-wilk_acc.xlsx")

write_xlsx(accuracy_mgg, "mgg_acc.xlsx")
write_xlsx(wilcoxon_exact, "wilcoxon_exact_acc.xlsx")
write_xlsx(t_test, "t_test_acc.xlsx")



