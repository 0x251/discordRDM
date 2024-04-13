# discordRDM
![image](https://github.com/0x251/discordRDM/assets/159673477/b8bb0e2f-687c-4e7f-a4d7-85794d9327d6)


# Setup
First, enter config.json and you will see a bunch of options, you will only need to configure two for this to work correctly. the two options you will need to configure are called ``Auth-Token`` and ``Session-Token``. You might be asking how do I get these two, well all you need to do is follow these steps.
- First log into Discord, via app or browser
- Second join a voice channel, for easy to get both that you need
- Now hit ``ctrl+i`` on you're keyboard and head over to the network tab
- Afterwards, you want to start an activity in the voice channel, you want to find a request that was sent to discord API that looks something like this ``https://discord.com/api/v9/activities/ID/ID``
- Now you want to click the payload section of that request and copy the item that says ``session_id`` it will look something like this (![image](https://github.com/0x251/discordRDM/assets/159673477/f0b0e2fb-8114-4efe-9a64-ad9dbd4139a8)
)
- Now you want to head over to the Headers section copy the Authorisation token, and replace ``Session-Token`` with the sessionID you copied and ``Auth-Token`` with the Authorisation token.
That is all you will need, sessionID will always expire when the client is closed, so you will need to grab a new sessionID when you close discord.

### Features
- Spam random activity's in discord channels that are full, or ones you aren't even in, This will annoy the VC users with a leave and join noise that it produces
- Spam soundboard noises in VC's that you have permissions too
- More to come 
