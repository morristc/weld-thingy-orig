# weldingcostestimator.py
#   A program to calculate the estimated cost of a welding project
# by: Thomas Morris

# global variables
laborRate = 15.0
salesTax = 0.06
veteranDiscount = 0.25

def main():
    weldingProcess = input("What welding process is being used? ")

    migStr = "mig"
    tigStr = "tig"
    stickStr = "stick"
    fluxCoreStr = "flux"

    if weldingProcess == migStr:
        print("You have selected the mig welding process.")
        mig()
    elif weldingProcess == fluxCoreStr:
        print("You have selected the flux core welding process.")
        fluxcore()
    elif weldingProcess == tigStr:
        print("You have selected the tig welding process.")
        tig()
    else:
        print("You must not be welding.")

# mig function
def mig():
    veteran = input("Is the customer a veteran? ")
    veteranYes = "y"
    # initial purchase
    rollPurchaseWeight = 2.0
    wireRollCost = 11.79
    costPlusTax = wireRollCost + (wireRollCost * salesTax)

    # weight prior to welding
    initialWireWeight = 2.0
    costPerPound =  (rollPurchaseWeight / costPlusTax)

    # gas variables
    gasTankSize = 125
    gasTankRentalCost = 80.00
    gasTankFillCost = 75.36
    gasCostPlusTax = (gasTankRentalCost + gasTankFillCost) + ((gasTankRentalCost + gasTankFillCost) * salesTax)
    gasFlowRate = 20.0
    gasCharge = (gasTankSize / gasCostPlusTax) * gasFlowRate

    # material cost (metal, etc)
    estimatedMaterialCost = eval(input("Enter material cost: "))

    # weld time
    estimatedWeldTime = eval(input("Enter weld time in hours: "))
    gasTotal = gasCharge * estimatedWeldTime
    laborTotal = laborRate * estimatedWeldTime

    # wire used
    postWeldWireWeight = eval(input("Enter post weld wire weight: "))
    wireUsed = initialWireWeight - postWeldWireWeight
    wireUseCost = (initialWireWeight - postWeldWireWeight) * costPerPound
    consumablesTotal = gasTotal + wireUseCost
    print(f'Wire use costs is ${wireUseCost:.2f} for {wireUsed:.2f} wire used.')

    # estimate total
    estimateTotal = (laborTotal + consumablesTotal + estimatedMaterialCost)
    estimateTotalWithDiscount = (estimateTotal * veteranDiscount)
    print(f'Labor: ${laborTotal:.2f}')
    print(f'Material: ${estimatedMaterialCost:.2f}')
    print(f'Consumables: ${consumablesTotal:.2f}')

    if veteran == veteranYes:
        print(f'Estimate total with discount: ${estimateTotalWithDiscount:.2f}')
    else:
        print(f'Estimate total: ${estimateTotal:.2f}')

# fluxcore function
def fluxcore():
    rollPurchaseWeight = eval(input("Enter roll purchase weight: "))
    initialWireWeight = eval(input("Enter initial wire weight: "))
    wireRollCost = eval(input("Enter cost of wire roll: "))
    estimatedMaterialCost = eval(input("Enter the estimated material cost: "))
    estimatedWeldTime = eval(input("Enter estimated weld time in hours: "))

    costPerPound =  (rollPurchaseWeight / wireRollCost)
    print("Wire cost per pound is: $", costPerPound)

    postWeldWireWeight = eval(input("Enter post weld wire weight: "))
    wireUseCost = (initialWireWeight - postWeldWireWeight) * costPerPound
    estimateTotal = ((laborRate * estimatedWeldTime) + wireUseCost + estimatedMaterialCost)

    print("Estimate total is: $", estimateTotal)

# tig function
def tig():
    # tungsten rod
    tungstenPackSize = eval(input("Enter tungsten pack size: "))
    tungstenPurchasePrice = eval(input("Enter tungsten pack purchase price: "))
    pricePerTungstenRod = tungstenPackSize / tungstenPurchasePrice
    print("Price per rod is ", pricePerTungstenRod)

    numberOfRodsUsed = eval(input("Enter the number of rods used: "))
    rodCostEstimate = numberOfRodsUsed * pricePerTungstenRod
    print("Rod cost estimate is: ", rodCostEstimate)

    # filler rod
    fillerRodInitialWeight = eval(input("Enter filler rod purchase weight: "))
    fillerRodCost = eval(input("Enter cost of filler rod pack: "))
    fillerRodCostPerPound = fillerRodInitialWeight / fillerRodCost
    print("Filler rod cost per pound is: $", fillerRodCostPerPound)
    postFillerRodWeight = eval(input("Enter post filler rod weight: "))
    fillerRodUsedCost = ((fillerRodInitialWeight - postFillerRodWeight) * fillerRodCostPerPound)

    # argon gas
    gasTankSize = eval(input("Enter the gas tank size (cf):"))
    gasTankCost = eval(input("Enter cost for full tank: "))
    gasFlowRate = eval(input("Enter gas flow rate (18-22): "))
    gasCharge = (gasTankSize / gasTankCost) * gasFlowRate
    print("Gas charge rate is: $", gasCharge)
    gasTotal = gasCharge * estimatedWeldTime
    print("Gas total is: $", gasTotal)

    # materials
    estimatedMaterialCost = eval(input("Enter the estimated material cost: "))

    # weld time
    estimatedWeldTime = eval(input("Enter estimated weld time in hours: "))

    # estimate total
    estimateTotal = ((laborRate * estimatedWeldTime) + estimatedMaterialCost + fillerRodCost + gasTotal)
main()
