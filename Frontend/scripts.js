// Searches for the username given in the prompt
// If found, opens the game page at their ID
// Otherwise TODO
function openUser() {
  userInput = prompt("What is your username?");
  fetch("http://localhost:5000/users/", { method: "GET" })
    .then((response) => response.json())
    .then((content) => {
      let found = false;
      for (let i = 0; i < content.length; i++) {
        if (content[i].name === userInput) {
          found = true;
          location.href = `/play/?user=${content[i].id}`;
        }
      }
      if (!found) {
        // TODO
        console.log("User not found :)");
      }
    });
}

// Returns the current user
function returnUser() {
  return new URLSearchParams(window.location.search).get("user");
}

var currentValues = {
  pointsTotal: 0,
  pointsSpent: 0,
  pointsGain: 0,
  pointsPassive: 0,
};

function fetchUpgrades(currentValues) {}

// function fetchUpgrades() {
//   // Fetch from backend
//   let upgradeArray = [
//     // This will be replaced by the fetch
//     { Name: "Steel Pickaxe", Effect: "ADD", Value: 5 },
//     { Name: "Electric Lantern", Effect: "MULTIPLY", Value: 2 },
//     { Name: "Gnome Assistants", Effect: "PASSIVE", Value: 1 },
//     { Name: "Good Meal", Effect: "EXPONENT", Value: 1 },
//   ];

//   miningValue = 0;
//   miningPassive = 0;
//   var miningAddition = 0;
//   var miningMultiply = 1;
//   var miningExponent = 1;

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
  fetchUpgrades(currentValues);
  var timeSinceLastClick = 60; // Time in seconds since the last click
  currentPoints += miningValue + miningPassive * timeSinceLastClick;
  console.log(`Current points: ${currentPoints}`);
  pointsUpdate(currentValues);
}

function buyUpgrade(name) {
  alert(`${name} was bought.`);
  updateUpgrades();
}

function updateUpgrades() {
  const inventoryList = document.getElementById("upgradeInventory");
  const shopList = document.getElementById("upgradeShop");
  inventoryList.innerHTML = "";
  shopList.innerHTML = "";
  let userUpgrades = fetchUpgrades();
  // Do a fetch of all possible upgrades (From upgrades table)
  let exampleUpgradeList = [
    { Name: "Steel Pickaxe", Effect: "ADD", Value: 5 },
    { Name: "Qubit Pickaxe", Effect: "ADD", Value: 25 },
    { Name: "Basic Lantern", Effect: "MULTIPLY", Value: 1.5 },
    { Name: "Electric Lantern", Effect: "MULTIPLY", Value: 2 },
    { Name: "Gnome Assistants", Effect: "PASSIVE", Value: 1 },
    { Name: "Good Meal", Effect: "EXPONENT", Value: 1 },
  ];

  for (let i = 0; i < exampleUpgradeList.length; i++) {
    found = false;
    for (let j = 0; j < userUpgrades.length; j++) {
      if (exampleUpgradeList[i].Name == userUpgrades[j].Name) {
        found = true;
        break;
      }
    }
    if (found) {
      const inventoryElement = document.createElement("li");
      inventoryElement.innerText = exampleUpgradeList[i].Name;
      inventoryList.appendChild(inventoryElement);
    } else {
      const shopElement = document.createElement("li");
      shopElement.innerText = exampleUpgradeList[i].Name;
      const elementButton = document.createElement("button");
      elementButton.innerText = "Buy";
      elementButton.addEventListener("click", () => {
        buyUpgrade(exampleUpgradeList[i].Name);
      });
      shopElement.appendChild(elementButton);
      shopList.appendChild(shopElement);
    }
  }
}
updateUpgrades();

function regularFetch() {
  console.log("A fetch would have been executed right now!");
  // This function will send a POST request every few seconds to update the USERS table
}
setInterval(regularFetch, 5000);
