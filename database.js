var stall1_dict ={
    "Name" : "Chicken Rice",
    "Operating Hours" : [["08","00","00"] , [16,"00","00"]],
    "Operating Days":[0,1,2,3,4,5],
    "Waiting Time" : 5,
    "Food available" :
        {   
            "Chicken Rice" : ["$5.00" , [0,1,2,3,4,5], ["08","00","00"],[17,"00","00"]],
            "Chicken Noodles" : ["$4.00", [0,1,2,3,5], [10,"00","00"],[17,"00","00"]],
            "Chicken Soup" : ["$3.00", [0,1,2,3,4,5], ["08","00","00"],[11,"00","00"]],
        }
    }

var stall2_dict ={
    "Name" : "McDonald's",
    "Operating Hours" : [["06",2,"00"] , [22,"00","00"]],
    "Operating Days":[0,1,2,4,5],
    "Waiting Time" : 3,
    "Food available" :
        {
            "2-Piece Chicken Meal" : ["$7.00" , [0,1,2,3,4,5], ["08","00","00"],[17,"00","00"]],
            "Big Breakfast" : ["$4.00", [1,2,3,4,5], ["06","00","00"],[11,"00","00"]],
            "Hershey's McFlurry" : ["$2.00", [0,1,2,3,4], ["06","00","00"],[22,"00","00"]],
        }
    }


var stall3_dict ={
    "Name" : "Mini Wok",
    "Operating Hours" : [[10,"00","00"] , [21,30,"00"]],
    "Operating Days":[2,3,4,5,6],
    "Waiting Time" : 8,
    "Food available" :
        {
            "Salted Fish Fried Rice" : ["$7.00" , [2,3,4,5], [10,"00","00"],[17,"00","00"]],
            "Pineapple Fish Fried Rice" : ["$8.00", [0,1,2,3,5], ["06","00","00"],[11,"00","00"]],
            "Chicken Fried Rice" : ["$6.00", [0,1,3,4,6], ["06","00","00"],[22,"00","00"]],
        }
    }
allStalls_dict = [stall1_dict, stall2_dict,stall3_dict]

