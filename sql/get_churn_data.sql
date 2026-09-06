SELECT
    c.customerID,
    c.gender,
    c.SeniorCitizen,
    c.Partner,
    c.Dependents,
    con.tenure,
    con.Contract,
    con.PaperlessBilling,
    con.PaymentMethod,
    con.MonthlyCharges,
    con.TotalCharges,
    MAX(CASE WHEN s.service_name = 'PhoneService' AND s.service_value = 'Yes' THEN 1 ELSE 0 END) AS PhoneService,
    MAX(CASE WHEN s.service_name = 'MultipleLines' AND s.service_value = 'Yes' THEN 1 ELSE 0 END) AS MultipleLines,
    MAX(CASE WHEN s.service_name = 'InternetService' AND s.service_value = 'DSL' THEN 1 ELSE 0 END) AS InternetService_DSL,
    MAX(CASE WHEN s.service_name = 'InternetService' AND s.service_value = 'Fiber optic' THEN 1 ELSE 0 END) AS InternetService_FiberOptic,
    MAX(CASE WHEN s.service_name = 'OnlineSecurity' AND s.service_value = 'Yes' THEN 1 ELSE 0 END) AS OnlineSecurity,
    MAX(CASE WHEN s.service_name = 'OnlineBackup' AND s.service_value = 'Yes' THEN 1 ELSE 0 END) AS OnlineBackup,
    MAX(CASE WHEN s.service_name = 'DeviceProtection' AND s.service_value = 'Yes' THEN 1 ELSE 0 END) AS DeviceProtection,
    MAX(CASE WHEN s.service_name = 'TechSupport' AND s.service_value = 'Yes' THEN 1 ELSE 0 END) AS TechSupport,
    MAX(CASE WHEN s.service_name = 'StreamingTV' AND s.service_value = 'Yes' THEN 1 ELSE 0 END) AS StreamingTV,
    MAX(CASE WHEN s.service_name = 'StreamingMovies' AND s.service_value = 'Yes' THEN 1 ELSE 0 END) AS StreamingMovies,
    con.Churn
FROM
    customers c
JOIN
    contracts con ON c.customerID = con.customerID
LEFT JOIN
    services s ON c.customerID = s.customerID
GROUP BY
    c.customerID;
