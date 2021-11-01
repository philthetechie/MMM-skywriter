Module.register("MMM-skywriter",{
	start: function() {
		this.sendSocketNotification('CONFIG', this.config);
		Log.info('Starting module: ' + this.name);
	},
    socketNotificationReceived: function(notification, payload) {
        Log.log(this.name + " received a socket notification: " + notification + " - Payload: " + payload);
		if (notification === "gesture") {
			if (this.config['notifications'][payload] !== 'undefined'){
				Log.log(this.name + "Gesture received: " + payload + ". Sending notification: " + this.config['notifications'][payload]);
				this.sendNotification(this.config['notifications'][payload], {});
			}
			else {
				Log.log(this.name + "Received unaassigned skywriter gesture: " + payload);
			}
		}

    },
});