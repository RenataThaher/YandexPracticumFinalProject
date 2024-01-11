Select c."login", COUNT(o.id) from "Couriers" as c
Left Join "Orders" as o on o."courierId" = c."id"
Group By c."login";