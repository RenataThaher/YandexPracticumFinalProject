Select "track",
       Case
           When "finished" = true Then 2
           When "cancelled" = true Then -1
           When "inDelivery" = true Then 1
           Else 0
       End as status
From "Orders";