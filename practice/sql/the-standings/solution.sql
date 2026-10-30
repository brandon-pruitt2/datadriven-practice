select category
  ,sum(total_amount) as total_amount 
  ,sum(quantity) as total_units
  ,rank() OVER (ORDER BY sum(quantity) DESC) as position
from transactions t
join products p 
  ON t.product_id = p.product_id
GROUP BY category
ORDER BY position ASC
