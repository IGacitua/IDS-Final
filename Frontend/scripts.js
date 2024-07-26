function pointsUpdate(currentValues) {
  const pointDisplay = document.getElementById("pointDisplay");
  pointDisplay.innerText = `Current Points: 
  ${currentValues.pointsTotal - currentValues.pointsSpent}`;
}

function calculatePoints(currentValues) {
  fetchUserUpgrades(currentValues);
  var timeSinceLastClick = 60; // Time in seconds since the last click
  currentValues.pointsTotal +=
    currentValues.pointsGain + currentValues.pointsPassive * timeSinceLastClick;
  console.log(
    `Current points: ${currentValues.pointsTotal - currentValues.pointDisplay}`
  );
  pointsUpdate(currentValues);
}

function buyUpgrade(name) {
  alert(`${name} was bought.`);
  updateUpgrades();
}

// function updateUpgrades() {
//   const inventoryList = document.getElementById("upgradeInventory");
//   const shopList = document.getElementById("upgradeShop");
//   inventoryList.innerHTML = "";
//   shopList.innerHTML = "";
//   let userUpgrades = fetchUserUpgrades();
//   // Do a fetch of all possible upgrades (From upgrades table)
//   let exampleUpgradeList = [
//     { Name: "Steel Pickaxe", Effect: "ADD", Value: 5 },
//     { Name: "Qubit Pickaxe", Effect: "ADD", Value: 25 },
//     { Name: "Basic Lantern", Effect: "MULTIPLY", Value: 1.5 },
//     { Name: "Electric Lantern", Effect: "MULTIPLY", Value: 2 },
//     { Name: "Gnome Assistants", Effect: "PASSIVE", Value: 1 },
//     { Name: "Good Meal", Effect: "EXPONENT", Value: 1 },
//   ];

//   for (let i = 0; i < exampleUpgradeList.length; i++) {
//     found = false;
//     for (let j = 0; j < userUpgrades.length; j++) {
//       if (exampleUpgradeList[i].Name == userUpgrades[j].Name) {
//         found = true;
//         break;
//       }
//     }
//     if (found) {
//       const inventoryElement = document.createElement("li");
//       inventoryElement.innerText = exampleUpgradeList[i].Name;
//       inventoryList.appendChild(inventoryElement);
//     } else {
//       const shopElement = document.createElement("li");
//       shopElement.innerText = exampleUpgradeList[i].Name;
//       const elementButton = document.createElement("button");
//       elementButton.innerText = "Buy";
//       elementButton.addEventListener("click", () => {
//         buyUpgrade(exampleUpgradeList[i].Name);
//       });
//       shopElement.appendChild(elementButton);
//       shopList.appendChild(shopElement);
//     }
//   }
// }
// updateUpgrades();

function regularFetch() {
  console.log("A fetch would have been executed right now!");
  // This function will send a POST request every few seconds to update the USERS table
}
setInterval(regularFetch, 5000);
