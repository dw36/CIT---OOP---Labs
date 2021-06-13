from mobile_device import MobileDevice
from repair_manager import RepairManager

def print_report(repair_manager):
    stats = repair_manager.get_repair_stats()

    print("Report for %s" % repair_manager.get_store_name())
    print("  Pending repairs: %d" % stats.get_num_pending_repairs())
    print("  Completed repairs: %d" % stats.get_num_completed_repairs())
    print("  Profit: $%.2f \n" % stats.get_total_profit())


def main():
    mikes_shop = RepairManager(" Mike’s Mobile Repair Shop")
    print_report(mikes_shop)


    davids_shop = RepairManager(" David's Mobile Repair Shop")
    phone1 = MobileDevice("Apple", "iPhone 1", "32GB", "broken screen", "2008-05-10", "ser356832")
    phone2 = MobileDevice("Apple", "iPhone 2", "64GB", "broken screen", "2009-06-14", "ser365453")
    phone3 = MobileDevice("Apple", "iPhone 3", "128GB", "broken screen", "2014-02-21", "ser356132")
    phone4 = MobileDevice("Apple", "iPhone 4", "256GB", "broken screen", "2014-05-16", "ser346832")
    phone5 = MobileDevice("Apple", "iPhone 5", "512GB", "broken screen", "2015-11-25", "ser359832")
    phone6 = MobileDevice("Apple", "iPhone 6", "1024GB", "broken screen", "2016-03-12", "ser356831")
    davids_shop.add_device(phone1)
    davids_shop.add_device(phone2)
    davids_shop.add_device(phone3)
    davids_shop.add_device(phone4)
    davids_shop.add_device(phone5)
    davids_shop.add_device(phone6)
    print_report(davids_shop)


    davids_shop.remove_device("ser356832")
    davids_shop.remove_device("ser365453")
    davids_shop.remove_device("ser356132")
    davids_shop.add_device(MobileDevice("Apple", "iPhone 7", "1024GB", "broken screen", "2017-03-12", "ser256831"))
    davids_shop.get_device("ser359832").set_price(59.9)
    davids_shop.get_device("ser356831").set_price(74.9)
    davids_shop.get_device("ser359832").complete_repair(24.5)
    davids_shop.get_device("ser356831").complete_repair(32.0)
    print_report(davids_shop)
    

if __name__ == "__main__":
    main()
