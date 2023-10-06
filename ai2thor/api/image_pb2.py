# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ai2thor/api/image.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ai2thor/api/image.proto',
  package='ai2thor.api',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x17\x61i2thor/api/image.proto\x12\x0b\x61i2thor.api\x1a\x1fgoogle/protobuf/timestamp.proto\"\xc9\x01\n\x0cImageRequest\x12\x19\n\x11image_source_name\x18\x01 \x01(\t\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0e\n\x06height\x18\x03 \x01(\x05\x12;\n\x0cpixel_format\x18\x04 \x01(\x0e\x32%.ai2thor.api.ImageRequest.PixelFormat\"B\n\x0bPixelFormat\x12\x17\n\x13PIXEL_FORMAT_BGR_U8\x10\x00\x12\x1a\n\x16PIXEL_FORMAT_DEPTH_U16\x10\x01\"`\n\x05Image\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0c\n\x04\x63ols\x18\x02 \x01(\x05\x12\x0c\n\x04rows\x18\x03 \x01(\x05\x12\x0c\n\x04\x64\x61ta\x18\x04 \x01(\x0c\"f\n\x11GetImageResponses\x12-\n\ttimestamp\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\"\n\x06images\x18\x02 \x03(\x0b\x32\x12.ai2thor.api.Image2\x98\x01\n\x0cImageService\x12;\n\x08GetImage\x12\x19.ai2thor.api.ImageRequest\x1a\x12.ai2thor.api.Image\"\x00\x12K\n\x0cGetAllImages\x12\x19.ai2thor.api.ImageRequest\x1a\x1e.ai2thor.api.GetImageResponses\"\x00\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_timestamp__pb2.DESCRIPTOR,])



_IMAGEREQUEST_PIXELFORMAT = _descriptor.EnumDescriptor(
  name='PixelFormat',
  full_name='ai2thor.api.ImageRequest.PixelFormat',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PIXEL_FORMAT_BGR_U8', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PIXEL_FORMAT_DEPTH_U16', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=209,
  serialized_end=275,
)
_sym_db.RegisterEnumDescriptor(_IMAGEREQUEST_PIXELFORMAT)


_IMAGEREQUEST = _descriptor.Descriptor(
  name='ImageRequest',
  full_name='ai2thor.api.ImageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='image_source_name', full_name='ai2thor.api.ImageRequest.image_source_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='width', full_name='ai2thor.api.ImageRequest.width', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='height', full_name='ai2thor.api.ImageRequest.height', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='pixel_format', full_name='ai2thor.api.ImageRequest.pixel_format', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _IMAGEREQUEST_PIXELFORMAT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=74,
  serialized_end=275,
)


_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='ai2thor.api.Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ai2thor.api.Image.timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cols', full_name='ai2thor.api.Image.cols', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rows', full_name='ai2thor.api.Image.rows', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='ai2thor.api.Image.data', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
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
  serialized_start=277,
  serialized_end=373,
)


_GETIMAGERESPONSES = _descriptor.Descriptor(
  name='GetImageResponses',
  full_name='ai2thor.api.GetImageResponses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='ai2thor.api.GetImageResponses.timestamp', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='images', full_name='ai2thor.api.GetImageResponses.images', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=375,
  serialized_end=477,
)

_IMAGEREQUEST.fields_by_name['pixel_format'].enum_type = _IMAGEREQUEST_PIXELFORMAT
_IMAGEREQUEST_PIXELFORMAT.containing_type = _IMAGEREQUEST
_IMAGE.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETIMAGERESPONSES.fields_by_name['timestamp'].message_type = google_dot_protobuf_dot_timestamp__pb2._TIMESTAMP
_GETIMAGERESPONSES.fields_by_name['images'].message_type = _IMAGE
DESCRIPTOR.message_types_by_name['ImageRequest'] = _IMAGEREQUEST
DESCRIPTOR.message_types_by_name['Image'] = _IMAGE
DESCRIPTOR.message_types_by_name['GetImageResponses'] = _GETIMAGERESPONSES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ImageRequest = _reflection.GeneratedProtocolMessageType('ImageRequest', (_message.Message,), {
  'DESCRIPTOR' : _IMAGEREQUEST,
  '__module__' : 'ai2thor.api.image_pb2'
  # @@protoc_insertion_point(class_scope:ai2thor.api.ImageRequest)
  })
_sym_db.RegisterMessage(ImageRequest)

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), {
  'DESCRIPTOR' : _IMAGE,
  '__module__' : 'ai2thor.api.image_pb2'
  # @@protoc_insertion_point(class_scope:ai2thor.api.Image)
  })
_sym_db.RegisterMessage(Image)

GetImageResponses = _reflection.GeneratedProtocolMessageType('GetImageResponses', (_message.Message,), {
  'DESCRIPTOR' : _GETIMAGERESPONSES,
  '__module__' : 'ai2thor.api.image_pb2'
  # @@protoc_insertion_point(class_scope:ai2thor.api.GetImageResponses)
  })
_sym_db.RegisterMessage(GetImageResponses)



_IMAGESERVICE = _descriptor.ServiceDescriptor(
  name='ImageService',
  full_name='ai2thor.api.ImageService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=480,
  serialized_end=632,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetImage',
    full_name='ai2thor.api.ImageService.GetImage',
    index=0,
    containing_service=None,
    input_type=_IMAGEREQUEST,
    output_type=_IMAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllImages',
    full_name='ai2thor.api.ImageService.GetAllImages',
    index=1,
    containing_service=None,
    input_type=_IMAGEREQUEST,
    output_type=_GETIMAGERESPONSES,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_IMAGESERVICE)

DESCRIPTOR.services_by_name['ImageService'] = _IMAGESERVICE

# @@protoc_insertion_point(module_scope)
