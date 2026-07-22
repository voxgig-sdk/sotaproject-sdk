# frozen_string_literal: true

# Typed models for the Sotaproject SDK.
#
# GENERATED from the API model: main.kit.entity.<e>.fields[] and per-op
# params (op.<name>.points[].args.params[]). Member types come from the
# canonical type sentinels via @voxgig/sdkgen canonToType (source of truth:
# @voxgig/apidef VALID_CANON). Ruby types are unenforced; these YARD
# annotations document the shapes. Do not edit by hand.

# Publication entity data model.
#
# @!attribute [rw] author
#   @return [String, nil]
#
# @!attribute [rw] category
#   @return [String, nil]
#
# @!attribute [rw] content
#   @return [String, nil]
#
# @!attribute [rw] id
#   @return [String, nil]
#
# @!attribute [rw] media
#   @return [Array, nil]
#
# @!attribute [rw] published_at
#   @return [String, nil]
#
# @!attribute [rw] title
#   @return [String, nil]
#
# @!attribute [rw] url
#   @return [String, nil]
Publication = Struct.new(
  :author,
  :category,
  :content,
  :id,
  :media,
  :published_at,
  :title,
  :url,
  keyword_init: true
)

# Request payload for Publication#list.
#
# @!attribute [rw] author
#   @return [String, nil]
#
# @!attribute [rw] category
#   @return [String, nil]
#
# @!attribute [rw] content
#   @return [String, nil]
#
# @!attribute [rw] id
#   @return [String, nil]
#
# @!attribute [rw] media
#   @return [Array, nil]
#
# @!attribute [rw] published_at
#   @return [String, nil]
#
# @!attribute [rw] title
#   @return [String, nil]
#
# @!attribute [rw] url
#   @return [String, nil]
PublicationListMatch = Struct.new(
  :author,
  :category,
  :content,
  :id,
  :media,
  :published_at,
  :title,
  :url,
  keyword_init: true
)

