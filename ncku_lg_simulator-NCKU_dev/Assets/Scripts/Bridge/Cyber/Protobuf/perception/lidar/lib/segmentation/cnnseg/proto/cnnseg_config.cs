// This file was generated by a tool; you should avoid making direct changes.
// Consider using 'partial classes' to extend these types
// Input: cnnseg_config.proto

#pragma warning disable 0612, 1591, 3021
namespace apollo.perception.lidar
{

    [global::ProtoBuf.ProtoContract()]
    public partial class CNNSegConfig : global::ProtoBuf.IExtensible
    {
        private global::ProtoBuf.IExtension __pbn__extensionData;
        global::ProtoBuf.IExtension global::ProtoBuf.IExtensible.GetExtensionObject(bool createIfMissing)
        {
            return global::ProtoBuf.Extensible.GetExtensionObject(ref __pbn__extensionData, createIfMissing);
        }
        public CNNSegConfig()
        {
            OnConstructor();
        }

        partial void OnConstructor();

        [global::ProtoBuf.ProtoMember(1)]
        [global::System.ComponentModel.DefaultValue(@"./data/models/cnnseg/param.conf")]
        public string param_file
        {
            get { return __pbn__param_file ?? @"./data/models/cnnseg/param.conf"; }
            set { __pbn__param_file = value; }
        }
        public bool ShouldSerializeparam_file()
        {
            return __pbn__param_file != null;
        }
        public void Resetparam_file()
        {
            __pbn__param_file = null;
        }
        private string __pbn__param_file;

        [global::ProtoBuf.ProtoMember(2)]
        [global::System.ComponentModel.DefaultValue(@"./data/models/cnnseg/deploy.prototxt")]
        public string proto_file
        {
            get { return __pbn__proto_file ?? @"./data/models/cnnseg/deploy.prototxt"; }
            set { __pbn__proto_file = value; }
        }
        public bool ShouldSerializeproto_file()
        {
            return __pbn__proto_file != null;
        }
        public void Resetproto_file()
        {
            __pbn__proto_file = null;
        }
        private string __pbn__proto_file;

        [global::ProtoBuf.ProtoMember(3)]
        [global::System.ComponentModel.DefaultValue(@"./data/models/cnnseg/deploy.caffemodel")]
        public string weight_file
        {
            get { return __pbn__weight_file ?? @"./data/models/cnnseg/deploy.caffemodel"; }
            set { __pbn__weight_file = value; }
        }
        public bool ShouldSerializeweight_file()
        {
            return __pbn__weight_file != null;
        }
        public void Resetweight_file()
        {
            __pbn__weight_file = null;
        }
        private string __pbn__weight_file;

        [global::ProtoBuf.ProtoMember(4)]
        [global::System.ComponentModel.DefaultValue(@"./data/models/cnnseg/engine.conf")]
        public string engine_file
        {
            get { return __pbn__engine_file ?? @"./data/models/cnnseg/engine.conf"; }
            set { __pbn__engine_file = value; }
        }
        public bool ShouldSerializeengine_file()
        {
            return __pbn__engine_file != null;
        }
        public void Resetengine_file()
        {
            __pbn__engine_file = null;
        }
        private string __pbn__engine_file;

        [global::ProtoBuf.ProtoMember(5)]
        [global::System.ComponentModel.DefaultValue(@"./data/models/cnnseg/paddle_param.conf")]
        public string paddle_param_file
        {
            get { return __pbn__paddle_param_file ?? @"./data/models/cnnseg/paddle_param.conf"; }
            set { __pbn__paddle_param_file = value; }
        }
        public bool ShouldSerializepaddle_param_file()
        {
            return __pbn__paddle_param_file != null;
        }
        public void Resetpaddle_param_file()
        {
            __pbn__paddle_param_file = null;
        }
        private string __pbn__paddle_param_file;

        [global::ProtoBuf.ProtoMember(6)]
        [global::System.ComponentModel.DefaultValue(@"./data/models/cnnseg/model")]
        public string paddle_proto_file
        {
            get { return __pbn__paddle_proto_file ?? @"./data/models/cnnseg/model"; }
            set { __pbn__paddle_proto_file = value; }
        }
        public bool ShouldSerializepaddle_proto_file()
        {
            return __pbn__paddle_proto_file != null;
        }
        public void Resetpaddle_proto_file()
        {
            __pbn__paddle_proto_file = null;
        }
        private string __pbn__paddle_proto_file;

        [global::ProtoBuf.ProtoMember(7)]
        [global::System.ComponentModel.DefaultValue(@"./data/models/cnnseg/params")]
        public string paddle_weight_file
        {
            get { return __pbn__paddle_weight_file ?? @"./data/models/cnnseg/params"; }
            set { __pbn__paddle_weight_file = value; }
        }
        public bool ShouldSerializepaddle_weight_file()
        {
            return __pbn__paddle_weight_file != null;
        }
        public void Resetpaddle_weight_file()
        {
            __pbn__paddle_weight_file = null;
        }
        private string __pbn__paddle_weight_file;

        [global::ProtoBuf.ProtoMember(8)]
        [global::System.ComponentModel.DefaultValue(false)]
        public bool use_paddle
        {
            get { return __pbn__use_paddle ?? false; }
            set { __pbn__use_paddle = value; }
        }
        public bool ShouldSerializeuse_paddle()
        {
            return __pbn__use_paddle != null;
        }
        public void Resetuse_paddle()
        {
            __pbn__use_paddle = null;
        }
        private bool? __pbn__use_paddle;

    }

}

#pragma warning restore 0612, 1591, 3021
