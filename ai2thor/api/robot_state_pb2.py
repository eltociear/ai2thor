# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ai2thor/api/robot_state.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ai2thor/api/robot_state.proto',
  package='ai2thor.api',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1d\x61i2thor/api/robot_state.proto\x12\x0b\x61i2thor.api\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"(\n\x11RobotStateRequest\x12\x13\n\x0b\x63lient_name\x18\x01 \x01(\t\"\x8f\x01\n\nRobotState\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12)\n\x04\x62\x61se\x18\x02 \x01(\x0b\x32\x1b.ai2thor.api.RobotBaseState\x12\'\n\x03\x61rm\x18\x03 \x01(\x0b\x32\x1a.ai2thor.api.RobotArmState\"&\n\x03XYZ\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\t\n\x01z\x18\x03 \x01(\x02\"X\n\x0eRobotBaseState\x12\"\n\x08position\x18\x01 \x01(\x0b\x32\x10.ai2thor.api.XYZ\x12\"\n\x08rotation\x18\x02 \x01(\x0b\x32\x10.ai2thor.api.XYZ\"\x91\x01\n\rRobotArmState\x12\x15\n\rextension_pos\x18\x06 \x01(\x02\x12\x17\n\x0f\x65xtension_force\x18\x01 \x01(\x02\x12\x10\n\x08lift_pos\x18\x02 \x01(\x02\x12\x12\n\nlift_force\x18\x03 \x01(\x02\x12\x14\n\x0cwrist_degree\x18\x04 \x01(\x02\x12\x14\n\x0cgrip_percent\x18\x05 \x01(\x02\x32_\n\x11RobotStateService\x12J\n\rGetRobotState\x12\x1e.ai2thor.api.RobotStateRequest\x1a\x17.ai2thor.api.RobotState\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_ROBOTSTATEREQUEST = _descriptor.Descriptor(
  name='RobotStateRequest',
  full_name='ai2thor.api.RobotStateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='client_name', full_name='ai2thor.api.RobotStateRequest.client_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=111,
  serialized_end=151,
)


_ROBOTSTATE = _descriptor.Descriptor(
  name='RobotState',
  full_name='ai2thor.api.RobotState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ai2thor.api.RobotState.timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='base', full_name='ai2thor.api.RobotState.base', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='arm', full_name='ai2thor.api.RobotState.arm', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=154,
  serialized_end=297,
)


_XYZ = _descriptor.Descriptor(
  name='XYZ',
  full_name='ai2thor.api.XYZ',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='ai2thor.api.XYZ.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='y', full_name='ai2thor.api.XYZ.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='z', full_name='ai2thor.api.XYZ.z', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=299,
  serialized_end=337,
)


_ROBOTBASESTATE = _descriptor.Descriptor(
  name='RobotBaseState',
  full_name='ai2thor.api.RobotBaseState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='ai2thor.api.RobotBaseState.position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rotation', full_name='ai2thor.api.RobotBaseState.rotation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=339,
  serialized_end=427,
)


_ROBOTARMSTATE = _descriptor.Descriptor(
  name='RobotArmState',
  full_name='ai2thor.api.RobotArmState',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='extension_pos', full_name='ai2thor.api.RobotArmState.extension_pos', index=0,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='extension_force', full_name='ai2thor.api.RobotArmState.extension_force', index=1,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lift_pos', full_name='ai2thor.api.RobotArmState.lift_pos', index=2,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lift_force', full_name='ai2thor.api.RobotArmState.lift_force', index=3,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='wrist_degree', full_name='ai2thor.api.RobotArmState.wrist_degree', index=4,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='grip_percent', full_name='ai2thor.api.RobotArmState.grip_percent', index=5,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=430,
  serialized_end=575,
)

_ROBOTSTATE.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_ROBOTSTATE.fields_by_name['base'].message_type = _ROBOTBASESTATE
_ROBOTSTATE.fields_by_name['arm'].message_type = _ROBOTARMSTATE
_ROBOTBASESTATE.fields_by_name['position'].message_type = _XYZ
_ROBOTBASESTATE.fields_by_name['rotation'].message_type = _XYZ
DESCRIPTOR.message_types_by_name['RobotStateRequest'] = _ROBOTSTATEREQUEST
DESCRIPTOR.message_types_by_name['RobotState'] = _ROBOTSTATE
DESCRIPTOR.message_types_by_name['XYZ'] = _XYZ
DESCRIPTOR.message_types_by_name['RobotBaseState'] = _ROBOTBASESTATE
DESCRIPTOR.message_types_by_name['RobotArmState'] = _ROBOTARMSTATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RobotStateRequest = _reflection.GeneratedProtocolMessageType('RobotStateRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROBOTSTATEREQUEST,
  '__module__' : 'ai2thor.api.robot_state_pb2'
  # @@protoc_insertion_point(class_scope:ai2thor.api.RobotStateRequest)
  })
_sym_db.RegisterMessage(RobotStateRequest)

RobotState = _reflection.GeneratedProtocolMessageType('RobotState', (_message.Message,), {
  'DESCRIPTOR' : _ROBOTSTATE,
  '__module__' : 'ai2thor.api.robot_state_pb2'
  # @@protoc_insertion_point(class_scope:ai2thor.api.RobotState)
  })
_sym_db.RegisterMessage(RobotState)

XYZ = _reflection.GeneratedProtocolMessageType('XYZ', (_message.Message,), {
  'DESCRIPTOR' : _XYZ,
  '__module__' : 'ai2thor.api.robot_state_pb2'
  # @@protoc_insertion_point(class_scope:ai2thor.api.XYZ)
  })
_sym_db.RegisterMessage(XYZ)

RobotBaseState = _reflection.GeneratedProtocolMessageType('RobotBaseState', (_message.Message,), {
  'DESCRIPTOR' : _ROBOTBASESTATE,
  '__module__' : 'ai2thor.api.robot_state_pb2'
  # @@protoc_insertion_point(class_scope:ai2thor.api.RobotBaseState)
  })
_sym_db.RegisterMessage(RobotBaseState)

RobotArmState = _reflection.GeneratedProtocolMessageType('RobotArmState', (_message.Message,), {
  'DESCRIPTOR' : _ROBOTARMSTATE,
  '__module__' : 'ai2thor.api.robot_state_pb2'
  # @@protoc_insertion_point(class_scope:ai2thor.api.RobotArmState)
  })
_sym_db.RegisterMessage(RobotArmState)



_ROBOTSTATESERVICE = _descriptor.ServiceDescriptor(
  name='RobotStateService',
  full_name='ai2thor.api.RobotStateService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=577,
  serialized_end=672,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetRobotState',
    full_name='ai2thor.api.RobotStateService.GetRobotState',
    index=0,
    containing_service=None,
    input_type=_ROBOTSTATEREQUEST,
    output_type=_ROBOTSTATE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ROBOTSTATESERVICE)

DESCRIPTOR.services_by_name['RobotStateService'] = _ROBOTSTATESERVICE

# @@protoc_insertion_point(module_scope)
