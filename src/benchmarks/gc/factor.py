# Case 1 - using pinned handle
# Out of 1000 objects, a survived and b is pinned
# 
# Case 2 - using POH
# Out of 1000 - b objects, a - b survived 
# Out of b object, b object survived and b is pinned
#
# In case 2 - the total survived object is (a - b) + b = a
#             the total pinned object is b
#
# So it is conceptually an apple to apple comparison
#
for a in range(1, 100):
    if 1000 % a == 0:
        for b in range(1, a):
            if a % b == 0:
                if ((1000 - b) % (a - b) == 0):
                    pin_sohsi = 1000 // a
                    pin_sohpi = a // b
                    poh_sohsi = (1000 - b) // (a - b)
                    poh_pohar = b
                    print("  2gb_pin_%s_%s:" % (a, b));
                    print("    arguments:");
                    print("      tc: 6");
                    print("      tagb: 100");
                    print("      tlgb: 2");
                    print("      lohar: 0");
                    print("      pohar: 0");
                    print("      sohsr: 100-4000");
                    print("      pohsr: 100-4000");
                    print("      sohsi: %s" % pin_sohsi);
                    print("      lohsi: 0");
                    print("      pohsi: 0");
                    print("      sohpi: %s" % pin_sohpi);
                    print("      lohpi: 0");
                    print("      sohfi: 0");
                    print("      lohfi: 0");
                    print("      pohfi: 0");
                    print("      allocType: reference");
                    print("      testKind: time");
                    print("  2gb_poh_%s_%s:" % (a, b));
                    print("    arguments:");
                    print("      tc: 6");
                    print("      tagb: 100");
                    print("      tlgb: 2");
                    print("      lohar: 0");
                    print("      pohar: %s" % poh_pohar);
                    print("      sohsr: 100-4000");
                    print("      pohsr: 100-4000");
                    print("      sohsi: %s" % poh_sohsi);
                    print("      lohsi: 0");
                    print("      pohsi: 1");
                    print("      sohpi: 0");
                    print("      lohpi: 0");
                    print("      sohfi: 0");
                    print("      lohfi: 0");
                    print("      pohfi: 0");
                    print("      allocType: reference");
                    print("      testKind: time");