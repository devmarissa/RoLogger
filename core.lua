-- n_arclogger
-- by n_arc


-- Setting Webhook Variables
local baseObj=script.Parent
local config=require(baseObj)
local webhook=config.WebhookURL
local cat=config.Category
local send=require(1636427267)

-- Sets Embed Values
function chatEmbed(pl,msg,rec)
	return{
		title=pl.Name,
		description=msg,
	}
end

-- Event Firings
function playerAdd(player)
	player.Chatted:Connect(function(...)
		send(webhook,nil,{chatEmbed(player,...)},cat)
	end)
end

-- Adds Players
game.Players.PlayerAdded:connect(playerAdd)
for i,player in pairs(game.Players:children()) do
	playerAdd(player)
end