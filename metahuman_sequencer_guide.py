# Need to initiate an object for the level which is done below:
# ref - https://docs.unrealengine.com/5.0/en-US/PythonAPI/class/EditorActorSubsystem.html?highlight=editoractorsubsystem#unreal.EditorActorSubsystem

level_util = unreal.EditorActorSubsystem()

# This is how you get all the actors from the level
actors = level_util.get_all_level_actors()
# You could also use level_util.get_selected_level_actors()[0] to get just the selected actor

sk_mesh = level_util.get_selected_level_actors()[0]

sk_mesh.skeletal_mesh_component()

https://docs.unrealengine.com/5.0/en-US/python-scripting-in-sequencer-in-unreal-engine/



# ADD A NEW LEVEL SEQUENCE AND ADD METAHUMAN (selected from viewport) TO IT

# Get asset tools
asset_tools = unreal.AssetToolsHelpers.get_asset_tools()

# Create a Level Sequence with name LevelSequenceName in root content folder
level_sequence = unreal.AssetTools.create_asset(asset_tools, asset_name = "LevelSequenceName", package_path = "/Game/Sequences/", asset_class = unreal.LevelSequence, factory = unreal.LevelSequenceFactoryNew())

#Note: The /Game folder mentioned above in path is the Content folder for the current project

#In case the level sequence is already created, you can get the level sequence as follows
level_sequence = unreal.load_asset("/Game/Sequences/LevelSequenceName")

# Then open it in Sequencer
unreal.LevelSequenceEditorBlueprintLibrary.open_level_sequence(level_sequence)

# Create a frame rate object and set to the desired fps number, default is 30fps
frame_rate = unreal.FrameRate(numerator = 60, denominator = 1)

# Set the display rate
level_sequence.set_display_rate(frame_rate)

# Set the playback range to 20-200
level_sequence.set_playback_start(0)
level_sequence.set_playback_end(600)

# Get the Actor subsystem to grab a selected actor
actor_system = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)

# Get the selected actor
actor = actor_system.get_selected_level_actors()[0]

# Add actor to level as a possessable
actor_binding = level_sequence.add_possessable(actor)

# Refresh to visually see the new binding added
unreal.LevelSequenceEditorBlueprintLibrary.refresh_current_level_sequence()

#The only way to get the components on a metahuman body, this will give a list of skeletal mesh components in the metahuman
actor.get_components_by_class(unreal.SkeletalMeshComponent)

#Using the above to get "Body" skeletal component of the actor
actor_body = None
for component in actor.get_components_by_class(unreal.SkeletalMeshComponent):
	if component.get_fname() == "Body":
		actor_body = component

#Adding it to the sequence as a possessable
component_binding = level_sequence.add_possessable(actor_body)

# Refresh to visually see the new binding added
unreal.LevelSequenceEditorBlueprintLibrary.refresh_current_level_sequence()


#CONTROL RIG IN SEQUENCER
#https://docs.unrealengine.com/5.0/en-US/python-scripting-for-animating-with-control-rig-in-unreal-engine/

# Get the Editor world
editor_subsytem = unreal.UnrealEditorSubsystem()
world = editor_subsytem.get_editor_world()

#Using this to load metahuman control rig
rig = unreal.load_asset("/Game/MetaHumans/Common/Common/MetaHuman_ControlRig")

#Get the rig class
rig_class = rig.get_control_rig_class()

# Using the level sequence and actor binding, we can either find or create a control rig track from the class
rig_track = unreal.ControlRigSequencerLibrary.find_or_create_control_rig_track(world, level_sequence, rig_class, component_binding)

# Tracks are composed of sections
rig_section = rig_track.get_sections()[0]

# Sections are composed of channels which contain the actual data!
rig_channels = rig_section.get_all_channels()

# To get the name of a particular channel, index represents the index of the channel
print(rig_channels[index].channel_name)

#ALL THE METAHUMAN RIG CONTROLS
rig_controls = ["global_ctrl",
"root_ctrl",
"body_offset_ctrl",
"thigh_l_fk_ctrl",
"calf_l_fk_ctrl",
"foot_l_fk_ctrl",
"ball_l_fk_ctrl",
"bigtoe_01_l_ctrl",
"bigtoes_02_l_ctrl",
"indextoe_01_l_ctrl",
"indextoe_02_l_ctrl",
"middletoe_01_l_ctrl",
"middletoe_02_l_ctrl",
"ringtoe_01_l_ctrl",
"ringtoe_02_l_ctrl",
"littletoe_01_l_ctrl",
"littletoe_02_l_ctrl",
"foot_l_ik_ctrl",
"ball_l_ik_ctrl",
"foot_bk1_l_ctrl",
"foot_roll_l_ctrl",
"tip_l_ctrl",
"heel_l_ctrl",
"leg_l_pv_ik_ctrl",
"thigh_r_fk_ctrl",
"calf_r_fk_ctrl",
"foot_r_fk_ctrl",
"ball_r_fk_ctrl",
"bigtoe_01_r_ctrl",
"bigtoes_02_r_ctrl",
"indextoe_01_r_ctrl",
"indextoe_02_r_ctrl",
"middletoe_01_r_ctrl",
"middletoe_02_r_ctrl",
"ringtoe_01_r_ctrl",
"ringtoe_02_r_ctrl",
"littletoe_01_r_ctrl",
"littletoe_02_r_ctrl",
"foot_r_ik_ctrl",
"ball_r_ik_ctrl",
"foot_bk1_r_ctrl",
"foot_roll_r_ctrl",
"tip_r_ctrl",
"heel_r_ctrl",
"leg_r_pv_ik_ctrl",
"upperarm_l_fk_ctrl",
"lowerarm_l_fk_ctrl",
"hand_l_fk_ctrl",
"thumb_01_l_ctrl",
"thumb_02_l_ctrl",
"thumb_03_l_ctrl",
"index_metacarpal_l_ctrl",
"index_01_l_ctrl",
"index_02_l_ctrl",
"index_03_l_ctrl",
"middle_metacarpal_l_ctrl",
"middle_01_l_ctrl",
"middle_02_l_ctrl",
"middle_03_l_ctrl",
"ring_metacarpal_l_ctrl",
"ring_01_l_ctrl",
"ring_02_l_ctrl",
"ring_03_l_ctrl",
"pinky_metacarpal_l_ctrl",
"pinky_01_l_ctrl",
"pinky_02_l_ctrl",
"pinky_03_l_ctrl",
"hand_l_ik_ctrl",
"arm_l_pv_ik_ctrl",
"upperarm_r_fk_ctrl",
"lowerarm_r_fk_ctrl",
"hand_r_fk_ctrl",
"thumb_01_r_ctrl",
"thumb_02_r_ctrl",
"thumb_03_r_ctrl",
"index_metacarpal_r_ctrl",
"index_01_r_ctrl",
"index_02_r_ctrl",
"index_03_r_ctrl",
"middle_metacarpal_r_ctrl",
"middle_01_r_ctrl",
"middle_02_r_ctrl",
"middle_03_r_ctrl",
"ring_metacarpal_r_ctrl",
"ring_01_r_ctrl",
"ring_02_r_ctrl",
"ring_03_r_ctrl",
"pinky_metacarpal_r_ctrl",
"pinky_01_r_ctrl",
"pinky_02_r_ctrl",
"pinky_03_r_ctrl",
"hand_r_ik_ctrl",
"arm_r_pv_ik_ctrl",
"body_ctrl",
"hips_ctrl",
"hips_tan_ctrl",
"spine_01_ctrl",
"spine_02_ctrl",
"spine_03_ctrl",
"head_ctrl",
"clavicle_l_ctrl",
"clavicle_r_ctrl",
"neck_01_ctrl",
"neck_02_ctrl",
"chest_ctrl",
"chest_tan_ctrl"
]


# These are used to append to the above controls to get the exact variables to manipulate
location_controls = [".Location.X",
".Location.Y",
".Location.Z"]

rotation_controls = [".Rotation.X",
".Rotation.Y",
".Rotation.Z"]

scale_controls = [".Scale.X",
".Scale.Y",
".Scale.Z"]

# Finding a particular channel index
for i in range(len(rig_channels)):
	if rig_controls[1]+location_controls[0] in str(rig_channels[i].channel_name):
		print(rig_channels[i].channel_name)
		print(i)

# Storing the important indexes of controls as a dictionary
rig_index_dict = {}
for ctrl in rig_controls:
	for item in location_controls+rotation_controls+scale_controls:
		for channel in rig_channels:
			if (ctrl+item == channel.channel_name):
				rig_index_dict[channel.channel_name] = rig_channels.index(channel)


# Channels are often composed of some (optional) default values and keys.
# To get the value of the keys
print(rig_channels[index].get_keys())

# To get the default value
print(rig_channels[index].get_default())

# To add a key
# add_key takes two parameters, first is the frame number denoted by unreal.FrameNumber(value), and second is the value itself
rig_channels[index].add_key(unreal.FrameNumber(0),1)

# KEYING ALL THE FRAMES
# Get level sequence start and end frame
start_frame = level_sequence.get_playback_start()
end_frame = level_sequence.get_playback_end()

for i in range(end_frame):
	rig_channels[index].add_key(unreal.FrameNumber(i),1)












# Get the Control Rigs in Sequencer - returns a list of ControlRigSequencerBindingProxy
rig_proxies = unreal.ControlRigSequencerLibrary.get_control_rigs(level_sequence)

# Get frame 0
frame_num = unreal.FrameNumber(0)

# Grab the first proxy - let's assume it is the Mannequin_ControlRig
rig_proxy = rig_proxies[0]

# From the ControlRigSequencerBindingProxy, we can get the ControlRig object
rig = rig_proxy.control_rig

# Gets the local control values, each control type will have their own typed function
transform = unreal.ControlRigSequencerLibrary.get_local_control_rig_transform(level_sequence, rig, "body_ctrl", frame_num)
bool = unreal.ControlRigSequencerLibrary.get_local_control_rig_bool(level_sequence, rig, "twist_ctrl_vis", frame_num)

print(transform)
print(bool)
