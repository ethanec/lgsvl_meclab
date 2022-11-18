// This file was generated by a tool; you should avoid making direct changes.
// Consider using 'partial classes' to extend these types
// Input: ncut_param.proto

#pragma warning disable 0612, 1591, 3021
namespace apollo.perception.lidar
{

    [global::ProtoBuf.ProtoContract()]
    public partial class NCutSegmentationParam : global::ProtoBuf.IExtensible
    {
        private global::ProtoBuf.IExtension __pbn__extensionData;
        global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
        {
            return global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);
        }
        public NCutSegmentationParam()
        {
            OnConstructor();
        }

        partial void OnConstructor();

        [global::ProtoBuf.ProtoMember(1)]
        [global::System.ComponentModel.DefaultValue(80f)]
        public float grid_radius
        {
            get { return __pbn__grid_radius ?? 80f; }
            set { __pbn__grid_radius = value; }
        }
        public bool ShouldSerializegrid_radius()
        {
            return __pbn__grid_radius != null;
        }
        public void Resetgrid_radius()
        {
            __pbn__grid_radius = null;
        }
        private float? __pbn__grid_radius;

        [global::ProtoBuf.ProtoMember(2)]
        [global::System.ComponentModel.DefaultValue(2.5f)]
        public float height_threshold
        {
            get { return __pbn__height_threshold ?? 2.5f; }
            set { __pbn__height_threshold = value; }
        }
        public bool ShouldSerializeheight_threshold()
        {
            return __pbn__height_threshold != null;
        }
        public void Resetheight_threshold()
        {
            __pbn__height_threshold = null;
        }
        private float? __pbn__height_threshold;

        [global::ProtoBuf.ProtoMember(3)]
        [global::System.ComponentModel.DefaultValue(1f)]
        public float partition_cell_size
        {
            get { return __pbn__partition_cell_size ?? 1f; }
            set { __pbn__partition_cell_size = value; }
        }
        public bool ShouldSerializepartition_cell_size()
        {
            return __pbn__partition_cell_size != null;
        }
        public void Resetpartition_cell_size()
        {
            __pbn__partition_cell_size = null;
        }
        private float? __pbn__partition_cell_size;

        [global::ProtoBuf.ProtoMember(4)]
        [global::System.ComponentModel.DefaultValue(0.3f)]
        public float vehicle_filter_cell_size
        {
            get { return __pbn__vehicle_filter_cell_size ?? 0.3f; }
            set { __pbn__vehicle_filter_cell_size = value; }
        }
        public bool ShouldSerializevehicle_filter_cell_size()
        {
            return __pbn__vehicle_filter_cell_size != null;
        }
        public void Resetvehicle_filter_cell_size()
        {
            __pbn__vehicle_filter_cell_size = null;
        }
        private float? __pbn__vehicle_filter_cell_size;

        [global::ProtoBuf.ProtoMember(5)]
        [global::System.ComponentModel.DefaultValue(0.1f)]
        public float pedestrian_filter_cell_size
        {
            get { return __pbn__pedestrian_filter_cell_size ?? 0.1f; }
            set { __pbn__pedestrian_filter_cell_size = value; }
        }
        public bool ShouldSerializepedestrian_filter_cell_size()
        {
            return __pbn__pedestrian_filter_cell_size != null;
        }
        public void Resetpedestrian_filter_cell_size()
        {
            __pbn__pedestrian_filter_cell_size = null;
        }
        private float? __pbn__pedestrian_filter_cell_size;

        [global::ProtoBuf.ProtoMember(6)]
        [global::System.ComponentModel.DefaultValue(0.1f)]
        public float outlier_length
        {
            get { return __pbn__outlier_length ?? 0.1f; }
            set { __pbn__outlier_length = value; }
        }
        public bool ShouldSerializeoutlier_length()
        {
            return __pbn__outlier_length != null;
        }
        public void Resetoutlier_length()
        {
            __pbn__outlier_length = null;
        }
        private float? __pbn__outlier_length;

        [global::ProtoBuf.ProtoMember(7)]
        [global::System.ComponentModel.DefaultValue(0.1f)]
        public float outlier_width
        {
            get { return __pbn__outlier_width ?? 0.1f; }
            set { __pbn__outlier_width = value; }
        }
        public bool ShouldSerializeoutlier_width()
        {
            return __pbn__outlier_width != null;
        }
        public void Resetoutlier_width()
        {
            __pbn__outlier_width = null;
        }
        private float? __pbn__outlier_width;

        [global::ProtoBuf.ProtoMember(8)]
        [global::System.ComponentModel.DefaultValue(0.3f)]
        public float outlier_height
        {
            get { return __pbn__outlier_height ?? 0.3f; }
            set { __pbn__outlier_height = value; }
        }
        public bool ShouldSerializeoutlier_height()
        {
            return __pbn__outlier_height != null;
        }
        public void Resetoutlier_height()
        {
            __pbn__outlier_height = null;
        }
        private float? __pbn__outlier_height;

        [global::ProtoBuf.ProtoMember(9)]
        [global::System.ComponentModel.DefaultValue(3)]
        public uint outlier_min_num_points
        {
            get { return __pbn__outlier_min_num_points ?? 3; }
            set { __pbn__outlier_min_num_points = value; }
        }
        public bool ShouldSerializeoutlier_min_num_points()
        {
            return __pbn__outlier_min_num_points != null;
        }
        public void Resetoutlier_min_num_points()
        {
            __pbn__outlier_min_num_points = null;
        }
        private uint? __pbn__outlier_min_num_points;

        [global::ProtoBuf.ProtoMember(10)]
        [global::System.ComponentModel.DefaultValue(@"SpatioTemporalGroundDetector")]
        public string ground_detector
        {
            get { return __pbn__ground_detector ?? @"SpatioTemporalGroundDetector"; }
            set { __pbn__ground_detector = value; }
        }
        public bool ShouldSerializeground_detector()
        {
            return __pbn__ground_detector != null;
        }
        public void Resetground_detector()
        {
            __pbn__ground_detector = null;
        }
        private string __pbn__ground_detector;

        [global::ProtoBuf.ProtoMember(11)]
        [global::System.ComponentModel.DefaultValue(@"HdmapROIFilter")]
        public string roi_filter
        {
            get { return __pbn__roi_filter ?? @"HdmapROIFilter"; }
            set { __pbn__roi_filter = value; }
        }
        public bool ShouldSerializeroi_filter()
        {
            return __pbn__roi_filter != null;
        }
        public void Resetroi_filter()
        {
            __pbn__roi_filter = null;
        }
        private string __pbn__roi_filter;

        [global::ProtoBuf.ProtoMember(12)]
        [global::System.ComponentModel.DefaultValue(true)]
        public bool remove_ground_points
        {
            get { return __pbn__remove_ground_points ?? true; }
            set { __pbn__remove_ground_points = value; }
        }
        public bool ShouldSerializeremove_ground_points()
        {
            return __pbn__remove_ground_points != null;
        }
        public void Resetremove_ground_points()
        {
            __pbn__remove_ground_points = null;
        }
        private bool? __pbn__remove_ground_points;

        [global::ProtoBuf.ProtoMember(13)]
        [global::System.ComponentModel.DefaultValue(true)]
        public bool remove_roi
        {
            get { return __pbn__remove_roi ?? true; }
            set { __pbn__remove_roi = value; }
        }
        public bool ShouldSerializeremove_roi()
        {
            return __pbn__remove_roi != null;
        }
        public void Resetremove_roi()
        {
            __pbn__remove_roi = null;
        }
        private bool? __pbn__remove_roi;

        [global::ProtoBuf.ProtoMember(14)]
        public NCutParam ncut_param { get; set; }

    }

    [global::ProtoBuf.ProtoContract()]
    public partial class NCutParam : global::ProtoBuf.IExtensible
    {
        private global::ProtoBuf.IExtension __pbn__extensionData;
        global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
        {
            return global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);
        }
        public NCutParam()
        {
            OnConstructor();
        }

        partial void OnConstructor();

        [global::ProtoBuf.ProtoMember(1)]
        [global::System.ComponentModel.DefaultValue(80f)]
        public float grid_radius
        {
            get { return __pbn__grid_radius ?? 80f; }
            set { __pbn__grid_radius = value; }
        }
        public bool ShouldSerializegrid_radius()
        {
            return __pbn__grid_radius != null;
        }
        public void Resetgrid_radius()
        {
            __pbn__grid_radius = null;
        }
        private float? __pbn__grid_radius;

        [global::ProtoBuf.ProtoMember(2)]
        [global::System.ComponentModel.DefaultValue(1f)]
        public float connect_radius
        {
            get { return __pbn__connect_radius ?? 1f; }
            set { __pbn__connect_radius = value; }
        }
        public bool ShouldSerializeconnect_radius()
        {
            return __pbn__connect_radius != null;
        }
        public void Resetconnect_radius()
        {
            __pbn__connect_radius = null;
        }
        private float? __pbn__connect_radius;

        [global::ProtoBuf.ProtoMember(3)]
        [global::System.ComponentModel.DefaultValue(0.25f)]
        public float super_pixel_cell_size
        {
            get { return __pbn__super_pixel_cell_size ?? 0.25f; }
            set { __pbn__super_pixel_cell_size = value; }
        }
        public bool ShouldSerializesuper_pixel_cell_size()
        {
            return __pbn__super_pixel_cell_size != null;
        }
        public void Resetsuper_pixel_cell_size()
        {
            __pbn__super_pixel_cell_size = null;
        }
        private float? __pbn__super_pixel_cell_size;

        [global::ProtoBuf.ProtoMember(4)]
        [global::System.ComponentModel.DefaultValue(5)]
        public uint num_cuts
        {
            get { return __pbn__num_cuts ?? 5; }
            set { __pbn__num_cuts = value; }
        }
        public bool ShouldSerializenum_cuts()
        {
            return __pbn__num_cuts != null;
        }
        public void Resetnum_cuts()
        {
            __pbn__num_cuts = null;
        }
        private uint? __pbn__num_cuts;

        [global::ProtoBuf.ProtoMember(5)]
        [global::System.ComponentModel.DefaultValue(0.4f)]
        public float ncuts_stop_threshold
        {
            get { return __pbn__ncuts_stop_threshold ?? 0.4f; }
            set { __pbn__ncuts_stop_threshold = value; }
        }
        public bool ShouldSerializencuts_stop_threshold()
        {
            return __pbn__ncuts_stop_threshold != null;
        }
        public void Resetncuts_stop_threshold()
        {
            __pbn__ncuts_stop_threshold = null;
        }
        private float? __pbn__ncuts_stop_threshold;

        [global::ProtoBuf.ProtoMember(6)]
        [global::System.ComponentModel.DefaultValue(0.3f)]
        public float ncuts_enable_classifier_threshold
        {
            get { return __pbn__ncuts_enable_classifier_threshold ?? 0.3f; }
            set { __pbn__ncuts_enable_classifier_threshold = value; }
        }
        public bool ShouldSerializencuts_enable_classifier_threshold()
        {
            return __pbn__ncuts_enable_classifier_threshold != null;
        }
        public void Resetncuts_enable_classifier_threshold()
        {
            __pbn__ncuts_enable_classifier_threshold = null;
        }
        private float? __pbn__ncuts_enable_classifier_threshold;

        [global::ProtoBuf.ProtoMember(7)]
        [global::System.ComponentModel.DefaultValue(1.5f)]
        public float sigma_space
        {
            get { return __pbn__sigma_space ?? 1.5f; }
            set { __pbn__sigma_space = value; }
        }
        public bool ShouldSerializesigma_space()
        {
            return __pbn__sigma_space != null;
        }
        public void Resetsigma_space()
        {
            __pbn__sigma_space = null;
        }
        private float? __pbn__sigma_space;

        [global::ProtoBuf.ProtoMember(8)]
        [global::System.ComponentModel.DefaultValue(1.5f)]
        public float sigma_feature
        {
            get { return __pbn__sigma_feature ?? 1.5f; }
            set { __pbn__sigma_feature = value; }
        }
        public bool ShouldSerializesigma_feature()
        {
            return __pbn__sigma_feature != null;
        }
        public void Resetsigma_feature()
        {
            __pbn__sigma_feature = null;
        }
        private float? __pbn__sigma_feature;

        [global::ProtoBuf.ProtoMember(9)]
        [global::System.ComponentModel.DefaultValue(0.2f)]
        public float skeleton_cell_size
        {
            get { return __pbn__skeleton_cell_size ?? 0.2f; }
            set { __pbn__skeleton_cell_size = value; }
        }
        public bool ShouldSerializeskeleton_cell_size()
        {
            return __pbn__skeleton_cell_size != null;
        }
        public void Resetskeleton_cell_size()
        {
            __pbn__skeleton_cell_size = null;
        }
        private float? __pbn__skeleton_cell_size;

        [global::ProtoBuf.ProtoMember(10)]
        [global::System.ComponentModel.DefaultValue(3)]
        public uint patch_size
        {
            get { return __pbn__patch_size ?? 3; }
            set { __pbn__patch_size = value; }
        }
        public bool ShouldSerializepatch_size()
        {
            return __pbn__patch_size != null;
        }
        public void Resetpatch_size()
        {
            __pbn__patch_size = null;
        }
        private uint? __pbn__patch_size;

        [global::ProtoBuf.ProtoMember(11)]
        [global::System.ComponentModel.DefaultValue(0.1f)]
        public float outlier_width_threshold
        {
            get { return __pbn__outlier_width_threshold ?? 0.1f; }
            set { __pbn__outlier_width_threshold = value; }
        }
        public bool ShouldSerializeoutlier_width_threshold()
        {
            return __pbn__outlier_width_threshold != null;
        }
        public void Resetoutlier_width_threshold()
        {
            __pbn__outlier_width_threshold = null;
        }
        private float? __pbn__outlier_width_threshold;

        [global::ProtoBuf.ProtoMember(12)]
        [global::System.ComponentModel.DefaultValue(0.1f)]
        public float outlier_height_threshold
        {
            get { return __pbn__outlier_height_threshold ?? 0.1f; }
            set { __pbn__outlier_height_threshold = value; }
        }
        public bool ShouldSerializeoutlier_height_threshold()
        {
            return __pbn__outlier_height_threshold != null;
        }
        public void Resetoutlier_height_threshold()
        {
            __pbn__outlier_height_threshold = null;
        }
        private float? __pbn__outlier_height_threshold;

        [global::ProtoBuf.ProtoMember(13)]
        [global::System.ComponentModel.DefaultValue(10)]
        public uint outlier_num_points_threshold
        {
            get { return __pbn__outlier_num_points_threshold ?? 10; }
            set { __pbn__outlier_num_points_threshold = value; }
        }
        public bool ShouldSerializeoutlier_num_points_threshold()
        {
            return __pbn__outlier_num_points_threshold != null;
        }
        public void Resetoutlier_num_points_threshold()
        {
            __pbn__outlier_num_points_threshold = null;
        }
        private uint? __pbn__outlier_num_points_threshold;

        [global::ProtoBuf.ProtoMember(14)]
        [global::System.ComponentModel.DefaultValue(0.05f)]
        public float overlap_factor
        {
            get { return __pbn__overlap_factor ?? 0.05f; }
            set { __pbn__overlap_factor = value; }
        }
        public bool ShouldSerializeoverlap_factor()
        {
            return __pbn__overlap_factor != null;
        }
        public void Resetoverlap_factor()
        {
            __pbn__overlap_factor = null;
        }
        private float? __pbn__overlap_factor;

        [global::ProtoBuf.ProtoMember(15)]
        [global::System.ComponentModel.DefaultValue(0.5f)]
        public float felzenszwalb_sigma
        {
            get { return __pbn__felzenszwalb_sigma ?? 0.5f; }
            set { __pbn__felzenszwalb_sigma = value; }
        }
        public bool ShouldSerializefelzenszwalb_sigma()
        {
            return __pbn__felzenszwalb_sigma != null;
        }
        public void Resetfelzenszwalb_sigma()
        {
            __pbn__felzenszwalb_sigma = null;
        }
        private float? __pbn__felzenszwalb_sigma;

        [global::ProtoBuf.ProtoMember(16)]
        [global::System.ComponentModel.DefaultValue(30f)]
        public float felzenszwalb_k
        {
            get { return __pbn__felzenszwalb_k ?? 30f; }
            set { __pbn__felzenszwalb_k = value; }
        }
        public bool ShouldSerializefelzenszwalb_k()
        {
            return __pbn__felzenszwalb_k != null;
        }
        public void Resetfelzenszwalb_k()
        {
            __pbn__felzenszwalb_k = null;
        }
        private float? __pbn__felzenszwalb_k;

        [global::ProtoBuf.ProtoMember(17)]
        [global::System.ComponentModel.DefaultValue(10)]
        public uint felzenszwalb_min_size
        {
            get { return __pbn__felzenszwalb_min_size ?? 10; }
            set { __pbn__felzenszwalb_min_size = value; }
        }
        public bool ShouldSerializefelzenszwalb_min_size()
        {
            return __pbn__felzenszwalb_min_size != null;
        }
        public void Resetfelzenszwalb_min_size()
        {
            __pbn__felzenszwalb_min_size = null;
        }
        private uint? __pbn__felzenszwalb_min_size;

    }

}

#pragma warning restore 0612, 1591, 3021
