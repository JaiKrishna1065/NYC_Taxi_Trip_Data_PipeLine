CREATE TABLE dim_payment (
    payment_type INT PRIMARY KEY
    case
        when payment_type in (1,2) then "Card"
        when payment_type in (4,5) then "Cash/UPI"
        else "Other"
    end as payment_mode
);
