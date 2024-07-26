// Returns the current user
function returnUser() {
  return new URLSearchParams(window.location.search).get("user");
}

function fetchUserUpgrades(currentValues) {
  let currentValues = {
    pointsTotal: 0,
    pointsSpent: 0,
    pointsGain: 5,
    pointsPassive: 1,
  };
  let user_upgrades = [];
  let all_upgrades = fetchAllUpgrades();

  let miningAddition = 0;
  let miningMultiply = 1;
  let miningExponent = 1;
  let miningPassive = 0;

  fetch(`http://localhost:5000/users/${returnUser()}/upgrades/`, {
    method: "GET",
  })
    .then((response) => response.json())
    .then((content) => {
      user_upgrades = content;
    });
  for (let i = 0; i < user_upgrades.length; i++) {
    if (user_upgrades[i].effect === "ADD") {
      console.log(`Addition upgrade: ${user_upgrades[i].name}`);
    } else if (upgradeArray[i].effect === "MULTIPLY") {
      console.log(`Multiplication upgrade: ${user_upgrades[i].name}`);
    } else if (upgradeArray[i].effect === "EXPONENT") {
      console.log(`Exponential upgrade: ${user_upgrades[i].name}`);
    } else if (upradeArray[i].effect === "PASSIVE") {
      console.log(`Passive upgrade: ${user_upgrades[i].name}`);
    } else {
      alert("Upgrade effect is not valid.");
    }
  }
  return currentValues;
}

function fetchAllUpgrades() {
  fetch(`http://localhost:5000/upgrades/`, { method: "GET" })
    .then((response) => response.json())
    .then((content) => {
      console.log(`All upgrades fetched.`);
      return content;
    });
}

//   for (let i = 0; i < upgradeArray.length; i++) {
//     if (upgradeArray[i].Effect === "ADD") {
//       miningAddition += upgradeArray[i].Value;
//     } else if (upgradeArray[i].Effect === "MULTIPLY") {
//       miningMultiply += upgradeArray[i].Value;
//     } else if (upgradeArray[i].Effect === "EXPONENT") {
//       miningExponent += upgradeArray[i].Value;
//     } else if (upgradeArray[i].Effect === "PASSIVE") {
//       miningPassive += upgradeArray[i].Value;
//     } else {
//       alert(
//         `Invalid upgrade effect: ${upgradeArray[i].Effect} from ${upgradeArray[i].Name} upgrade`
//       );
//     }
//   }
//   console.log(
//     `Addition: ${miningAddition}, Exponent: ${miningExponent}, Multiplier: ${miningMultiply}, Passive: ${miningPassive}`
//   );
//   miningValue = miningAddition ** miningExponent * miningMultiply;
//   return upgradeArray;
// }

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
