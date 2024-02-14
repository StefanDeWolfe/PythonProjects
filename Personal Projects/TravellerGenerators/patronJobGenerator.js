// var patron = ["","","","","","","","","","","",""];

var npcquirkpercent = 0.9;
var chancefacialhair = 0.2;
var chanceextracbtskill = 0.5;
var chanceextrabusskill = 0.4;

var patron = ["Individual","Hunter","Reporter/Media", "Explorer","Scientist","Industrialist","Local Police/Sy", "Local Corporate","Large Corporate","Intelligence","Military","Shady Organisation","MegaCorporation","Noble"];

var missiontype = ["Explore","Courier","Investigate","Penetrate","Protect","Liberate","Rescue","Sieze","Kidnap","Destroy","Military"];

var target=["Person", "Team", "Organisation", "Gadget/Eqpt", "Installation"];

var opposition = ["Nil","Elements","Opposing Person","Police/Sy","Opposing Org","Org Crime","Pirates","Military"];

var support = ["Nil","Supplies","Tech","Weapons","QRF","Spaceship"];

var legality = ["Legal","Marginal","Dubious","Illegal","Totally Illegal"];

var spacedistance = ["Current System", "Jump-1",  "Jump-2", "Jump-3", "Jump-5","Other side of subsector", "Neighbouring Subsector", "Neighbouring Sector"];

var systemdistance = ["Current world", "Inner System", "Belt", "Mid-System", "Outer System"];

var worlddistance = ["Local", "Continent", "Planet", "Moon", "Other World"];

var difficulty = ["Easy", "Average", "Difficult","Formidable","Impossible"];

var npcrace = ["Other Major Race", "Non-Human Minor Race", "Minor Human Race","Aslan","Vargr","Vilani","Vilani","Imperial", "Imperial", "Imperial", "Solomani"];

var npccareer = ["Civilian", "Bureaucrat", "Merchant", "Scientist","Entertainer", "Free Trader", "Explorer","Hunter", "Scout","Army", "Wet Navy", "Flyer", "Navy", "Marine"];


var npchumansubrace = ["White Skin", "Black Skin", "Olive Skin", "Brown Skin", "Short, with crumpled face", "Almond eyed"];

var npcmass = ["Gaunt", "Skinny", "Average","Overweight","Obese"];

var npcheight = ["Very Short", "Short", "Average","Tall","Very Tall"];

var npchairlength = ["Buzz-cut", "Short", "Average","Long","Bald"];

var npchaircolour = ["Grey/White", "Blonde", "Brown","Black","Coloured"];

var npchairstyle = ["Fanned", "Tiered", "Straight","Curly","Asymmetric"];

var npcfacialhair = ["Goatee", "Big scraggy beard", "Neat beard","Moustache","Handlebar Moustache"];


var npcwherefrom = ["Local", "Local", "Region", "Continent", "World", "Inner System", "Belt", "Outer System", "Neighbouring System", "Subsector", "Sector", "Neighbouring Sector", "Long way away!"];

var npcdisposition = ["Happy", "Sad", "Angry", "Nervous", "Cool", "Sinister", "Frightened", "Annoyed", "Businesslike", "Businesslike", "Very friendly","Amorous/Flirtatious"];

var npcmotivation = ["Fame","Career","Respect","Love & Romance","Wealth & Money","Helping Others", "Helping Self", "Helping Family/Nepotism","Greed", "Pain & Suffering","Control", "Safety & Security", "Protecting Family","Honour/Loyalty","Discovering","Knowledge","Health","Power","Creating/Creativity","Contributing","Approval/Acceptance","Curiosity","Idealism","Justice","Independence","Equality","Order","Lust","Social Interaction","Status","Tranquility","Vengeance", "Violence", "Stubborness", "Leadership", "Generousity", "Cowardice", "Fellowship", "Wisdom","Honesty", "Pomposity/Arrogance", "Ruthless", "Liar", "Harmless Eccentric", "Insane"];

var npccbtskills = ["Unarmed","Blade","Pistol","Rifle"];

var npcbusskills = ["Negotiation","Carousing","Computer","Streetwise","Liaison","Leader","Broker/Trader"]

var npcquirk = ["Facial tick", "Artifical arm", "Cyber-eye", "Cyber-visor", "Unpleasant odour", "Cough", "Sneezing", "Boils/warts", "Burns", "Scars", "Bandaged arm", "Limp", "Leg Brace", "Very smart", "Very unkempt", "Too many clothes", "Too few clothes", "Open weapon", "Drunk", "Dark glasses", "Breathing mask", "Large bag", "Notable headgear", "Notable gloves", "Notable clothes", "Pet/Familiar", "Personal bot","Obsessive note-taking", "Wants to come along","Hums","Whistles", "Accomplice","Strong accent","Long fingernails", "Notable hair","Very formal language","Poor Galanglic","Psionic","Wears a Psionic Helmet","Constantly on phone","Constantly on net", "Eschews technology","Has baby with them", "Bare feet", "Notable footwear", "Swears constantly", "Uses long words/old-fashioned speech", "Pious religious", "Evangelical religious", "Constantly eating","Darting eyes"];


function createAssignment() {
   var msg = "Your Assignment is: <br/><br/>";
   var stancedm = parseInt(document.assignment.systemstance.value);
   // msg += "Stance DM: "+stancedm+"<br/>";
   var patronidx = Math.floor(Math.random() * patron.length * 0.99);
   var missiontypeidx = Math.floor(Math.random() * missiontype.length * 0.99);
   missiontypeidx += stancedm;
   missiontypeidx = constrain(missiontypeidx, 0, missiontype.length-1);
   var targetidx = Math.floor(Math.random() * target.length * 0.99);
   var oppositionidx = Math.floor(Math.random() * opposition.length * 0.99);
   var supportidx = Math.floor(Math.random() * support.length * 0.99);
   var legalityidx = Math.floor(Math.random() * legality.length * 0.99);
   var spacedistanceidx = Math.floor(Math.random() * spacedistance.length * 0.99);
   var spaceradial = OneD6();
   var systemdistanceidx = Math.floor(Math.random() * systemdistance.length * 0.99);
   var difficultyidx = DFate()+DFate()+2;

   var relcostidx = (1+patronidx) * (1+missiontypeidx) * (1+oppositionidx) / (1+supportidx)  * (1+legalityidx) * (1+spacedistanceidx) * (1+systemdistanceidx)*(1+difficultyidx);
   var relcosthps = patron.length*missiontype.length*opposition.length/support.length*legality.length*spacedistance.length*systemdistance.length*5;
   var relcost = Math.floor(relcostidx / relcosthps * 100);
   relcostidx = Math.floor(relcostidx);

   msg += "Patron: "+ patron[patronidx]+ "<br/>";
   msg += "Mission Type: "+ missiontype[missiontypeidx]+ "<br/>";
   msg += "Mission Target: "+ target[targetidx]+ "<br/>";
   msg += "Opposition: "+ opposition[oppositionidx]+ "<br/>";
   msg += "Support: "+ support[supportidx]+ "<br/>";
   msg += "Legality: "+ legality[legalityidx]+ "<br/>";
   msg += "Space Distance: "+ spacedistance[spacedistanceidx]+ " (Radial Direction: "+spaceradial+")<br/>";
   msg += "System Location: "+ systemdistance[systemdistanceidx]+ "<br/>";
   msg += "Relative Reward: "+relcost +"% ("+relcostidx+")<br/>";
   msg += "Difficulty: "+difficulty[difficultyidx]+"<br/>";

// locations
// time

   msg += "<br/>"+createNPC('Patron');
   document.querySelector('div#output').innerHTML = msg;
}

function createAnNPC() {
   var msg = "<h4>NPC:</h4> <br/>"+createNPC('NPC');
   document.querySelector('div#output').innerHTML = msg;
}

function createNPC(npctype) {
   var msg = "";
   var str = TwoD6();
   var end = TwoD6();
   var dex = TwoD6();
   var intel = TwoD6();
   var edu = TwoD6();
   var soc = TwoD6();
   var strh = ToHex2(str);
   var endh = ToHex2(end);
   var dexh = ToHex2(dex);
   var inth = ToHex2(intel);
   var eduh = ToHex2(edu);
   var soch = ToHex2(soc);

   var upp = strh+""+endh+""+dexh+""+inth+""+eduh+""+soch;
   var age = 20 + Math.floor(Math.random() * Math.floor(60))+1;
   var dice = TwoD6();
   var gender = "Female";
   if ((dice > 2) && (dice < 7)) { gender = "Male"; }
   if ((dice > 6) && (dice < 11)) { gender = "Female"; }
   if (dice == 2) { gender = "Special"; }
   if (dice > 10) { gender = "Neuter"; }

   var height = DFate()+DFate()+2;
   var mass = DFate()+DFate()+2;
   var hairlength = DFate()+DFate()+2;
   var haircolour = DFate()+DFate()+2;
   var hairstyle = DFate()+DFate()+2;
   var facialhair = DFate()+DFate()+2;

   var careercode = Math.floor(Math.random() * npccareer.length * 0.99);
   var stancedm = parseInt(document.assignment.systemstance.value);
   careercode += stancedm;
   careercode = constrain(careercode, 0, npccareer.length-1);
   var career = npccareer[careercode];
   if (careercode > 7) {
      hairlength -= 3;
      if (hairlength < 0) { hairlength = 0; }
   }
   var rank = 3 + DFate()+DFate()+DFate();
   var racecode = Math.floor(Math.random() * npcrace.length * 0.99);
   var race = npcrace[racecode];
   var subrace = "";
   if ((race == "Imperial") || (race == "Solomani")) {
      subracecode = Math.floor(Math.random() * npchumansubrace.length * 0.99);
      subrace = npchumansubrace[subracecode];
   }
   var dispositioncode = Math.floor(Math.random() * npcdisposition.length * 0.99);
   var disposition = npcdisposition[dispositioncode];
   var primotivationcode = Math.floor(Math.random() * npcmotivation.length * 0.99);
   var primotivation = npcmotivation[primotivationcode];
   var primotivationlevel =  Math.floor(Math.random() * 10 * 0.99)+1;
   var secmotivationcode = Math.floor(Math.random() * npcmotivation.length * 0.99);
   var secmotivation = npcmotivation[secmotivationcode];
   var secmotivationlevel =  Math.floor(Math.random() * 10 * 0.99)+1;

   var quirk = "";
   var secquirk = "";
   if (Math.random() < npcquirkpercent) {
      var quirkcode = Math.floor(Math.random() * npcquirk.length * 0.99);
       quirk = npcquirk[quirkcode];
       if (Math.random() < npcquirkpercent) {
           var secquirkcode = Math.floor(Math.random() * npcquirk.length * 0.99);
           secquirk = npcquirk[secquirkcode];
       }
    }
   var wherefromidx = Math.floor(Math.random() * npcwherefrom.length * 0.99);
   var hairroll = 0;
   msg = npctype+" UPP: "+ upp + "<br/>";
   msg += npctype+" Age: "+ age + " yrs <br/>";
   msg += npctype+" Apparent Gender: " + gender + "<br/>";
   msg += npctype+" Height (for race): "+npcheight[height]+ "<br/>";
   msg += npctype+" Mass (for race): "+npcmass[mass]+ "<br/>";
   if (npctype != "Patron") {
      msg += npctype+" Career: " + career + "<br/>";
      msg += npctype+" Career Rank: " + rank + "<br/>";
   }
   msg += npctype+" Race: " + race + "<br/>";
   if (subrace != "") {
      msg += npctype+" Sub-race: "+subrace+"<br/>";
   }
   // major/minor race detail on pop-up
   if ((race == "Imperial") || (race == "Solomani")  || (race == "Vilani")) { 
      msg += npctype+" Hair Length: "+npchairlength[hairlength]+"<br/>";
      if (npchairlength[hairlength] != "bald") {
         msg += npctype+" Hair Style: "+npchairstyle[hairstyle]+"<br/>";
         msg += npctype+" Hair Colour: "+npchaircolour[haircolour]+"<br/>";
      }
      if (gender == "Male") {
        hairroll = Math.random();
         if (hairroll < chancefacialhair) {
            msg += npctype+" Facial Hair: "+npcfacialhair[facialhair]+"<br/>";
         }
      }
   }
   msg += npctype+" From: "+npcwherefrom[wherefromidx]+"<br/>";
   msg += npctype+" Disposition: "+disposition+"<br/>";
   msg += npctype+" Motivation 1: "+primotivation+"-"+primotivationlevel+"<br/>";
   msg += npctype+" Motivation 2: "+secmotivation+"-"+secmotivationlevel+"<br/>";
   if (quirk != "") {
      msg += npctype+" Quirk: "+quirk+"<br/>";
   }
   if (secquirk != "") {
      msg += npctype+" Secondary Quirk: "+secquirk+"<br/>";
   }
   var chancecbtskill = 0.1;
   var cbtskilltext = "";
   if (careercode > 7) { chancecbtskill = 1; }
   if (Math.random() < chancecbtskill) {
      var skillidx = Math.floor(Math.random() * npccbtskills.length * 0.99); 
      var skilllevel= 2 + DFate();
      cbtskilltext += npccbtskills[skillidx]+"-"+skilllevel;

      while (Math.random() < chanceextracbtskill) {
         skillidx = Math.floor(Math.random() * npccbtskills.length * 0.99); 
         skilllevel= 2 + DFate();
         cbtskilltext += ", "+npccbtskills[skillidx]+"-"+skilllevel;
      }
      msg += npctype + " Combat Skills: "+cbtskilltext+"<br/>";
   }
   
   var chancebusskill = 0.9;
   var busskilltext = "";
   if (careercode > 7) { chancebusskill = 0.3; }
   if (Math.random() < chancebusskill) {
      var skillidx = Math.floor(Math.random() * npcbusskills.length * 0.99); 
      var skilllevel= 2 + DFate();
      busskilltext += npcbusskills[skillidx]+"-"+skilllevel;

      while (Math.random() < chanceextrabusskill) {
         skillidx = Math.floor(Math.random() * npcbusskills.length * 0.99); 
         skilllevel= 2 + DFate();
         busskilltext += ", "+npcbusskills[skillidx]+"-"+skilllevel;
      }
      msg += npctype + " Business Skills: "+busskilltext+"<br/>";
   }

   if ((quirk == "Accomplice") || (secquirk == "Accomplice")) {
      msg += "<br/><h4>Accomplice</h4>";
      msg += createNPC('Accomplice');
      msg += "<br/>";
   }
   msg += "<hr/>";
   msg += npctype+" UPP: "+ upp + "  "+gender+ "  "+ age + " yrs <br/>";
   msg += race;
   if (subrace != "") {
      msg += " ( "+subrace+" ) ";
   }
   if (npctype != "Patron") {
      msg += ".  "+career;
      msg += " ( O" + rank + " )";
   }
   msg += ". "+npcheight[height]+ " height, "+npcmass[mass]+ " mass <br/>";
   if (cbtskilltext != "") {
        msg += cbtskilltext + "   ";
    }
    msg += busskilltext + "<br/><br/>";
   
   // major/minor race detail on pop-up
   if ((race == "Imperial") || (race == "Solomani")  || (race == "Vilani")) { 
      msg += "Their hair is "+npchairlength[hairlength]+". ";
      if (npchairlength[hairlength] != "bald") {
         msg += "It is "+npchaircolour[haircolour]+" and worn "+npchairstyle[hairstyle]+". ";         
      }
      if (gender == "Male") {
         if (hairroll < chancefacialhair) {
            msg += "They also have a "+npcfacialhair[facialhair];
         }
      }
      msg += "<br/>";
   }
   msg += "They are from the "+npcwherefrom[wherefromidx]+". ";
   msg += "They have a "+disposition+" disposition. Their motivations are "+primotivation+"-"+primotivationlevel+" and "+secmotivation+"-"+secmotivationlevel+". ";
   if (quirk != "") {
      msg += " They have "+quirk;
   }
   if (secquirk != "") {
      msg += " and "+secquirk;
   }
   
   msg += ". <br/>";
   
   
   return (msg);
}

function OneD6() {
   var temp = Math.floor(Math.random() * Math.floor(6) * 0.99)+1;
   return(temp);
}

function OneD12() {
   var temp = Math.floor(Math.random() * Math.floor(12) * 0.99)+1;
   return(temp);
}

function TwoD6() {
   var dice = OneD6()+OneD6();
   return(dice);
}
function DFate() {
   var dice = Math.floor(Math.random() * Math.floor(3) * 0.99)-1;
   return(dice);
}


function ToHex2(dec) {
   var hex = dec;
   if (dec == 10) { hex = "A"; }
   if (dec == 11) { hex = "B"; }
   if (dec == 12) { hex = "C"; }
   if (dec == 13) { hex = "D"; }
   if (dec == 14) { hex = "E"; }
   if (dec == 15) { hex = "F"; }
   if (dec == 16) { hex = "G"; }
   return(hex);
}


function constrain(val, lo, hi) {
   if (val < lo) { val = lo; }
   if (val > hi) { val = hi; }
   return(val);
}


function toggleassignment() {
    if (document.getElementById("assignment").style.display === "none") {
        document.getElementById("assignment").style.display = "block";
    } else {
        document.getElementById("assignment").style.display = "none";
    }
    return(false);
}

function hideassignment() {
    document.getElementById("assignment").style.display = "none";
    return(false);
}