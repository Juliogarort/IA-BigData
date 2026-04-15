# Carga el dataset mtcars
data(mtcars)
head(mtcars)


# 1. Visualizado de datos en gráfico
plot(mtcars$wt, mtcars$mpg,
     main="Datos originales",
     xlab="Peso (wt)", ylab="Millas por galón (mpg)")


# 2. Ajuste modelo de regresión y linea recta en gráfico
modelo <- lm(mpg ~ wt, data=mtcars)
abline(modelo, col='red')

# 3. Resumen del modelo
summary(modelo)


# 4. Calculo de RMSE y MAE del modelo
pr <- predict(modelo, mtcars)

mae <- mean(abs(mtcars$mpg - pr))
cat("MAE (Error medio) :", mae, "\n")

rmse <- sqrt(mean((mtcars$mpg - pr)^2))
cat("RMSE (Error típico) :", rmse, "\n")


# 5. Predicción de consumo esperado pa coche con wt de 3.2
predict(modelo, data.frame(wt = 3.2))

