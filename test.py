import user_manager 
import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="test.log",
    filemode="w"
)

if __name__ == "__main__":
    #creating object

    manager = user_manager.UserManager()

    #first case
    logging.info("Test case 1 RF 1")

    manager.add_user(1,"Santi")
    logging.info("Pass using debugger")
    logging.info("End test case")

    #second case
    logging.info("Test case 2 RF 2")

    user_1 = manager.find_user(1)

    logging.info(f"the user name is {user_1["name"]}")


    if user_1["name"] == "Santi":
        logging.info("")
    else:
        logging.error("failed")

    logging.info("End test case")

    #third case 
    logging.info("Test case 3 RF 3")

    manager.add_user(2,"Fabricio")
    manager.add_user(3,"Claudia")

    manager.delete_user(2)

    logging.info("passed using debbuger")

    logging.info("End test case")

    #fourth case         
    logging.info("Test case 4 RF 4")

    names = manager.get_all_names()
    if names == ["Santi", "Claudia"]:
        logging.info("PASSED")
    else:
        logging.error(f"Failed, the names returned are{names}")

    logging.info("End test case")


    logging.info("Test case 5 RNF 1")

    for i in range(1000):
        manager.add_user(i, f"Usuario #{str(i)}")

    logging.info("Passed")
    
    logging.info("End test case")




    




    
