WITH Totals as (
select category
  ,sum(total_amount) as total_amount 
  ,sum(quantity) as total_units
from transactions t
join products p 
  ON t.product_id = p.product_id
GROUP BY category
)

SELECT *
      ,rank() OVER (ORDER BY total_units DESC) as position
FROM Totals
ORDER BY position ASC
