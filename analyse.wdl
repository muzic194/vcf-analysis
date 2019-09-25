workflow myWorkflow {
    call analyseVcf
}

task analyseVcf {
    File inputFile
    
    runtime {
        docker: "muzic194/vcf-analyse"
    }
    command {
        python3 /script/analyse.py ${inputFile} out.json
    }
    output {
        File out = "out.json"
    }
}
