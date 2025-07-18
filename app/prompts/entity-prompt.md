# Database

- PostgresSQL
- Port: 54320
- Database: mydatabase
- Password: secret
- User: myuser

# Table

- Table의 정보는 Spring Data JPA 리소스로 이용한다.
- JPA Entity를 이용하여 Python 라이브러리로 처리한다.
- 또는 테이블 스키마를 이용한다.

## RawNews

```java
package com.funa.batchapp.news.entity;

import com.funa.common.entity.BaseEntity;
import jakarta.persistence.*;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

@Getter
@Setter
@NoArgsConstructor
@Entity
@Table(
    name = "batch_biz_raw_news",
    uniqueConstraints = {@UniqueConstraint(columnNames = {"news_id"})})
public class RawNews extends BaseEntity {

  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  private Long id;

  @Column(name = "news_id", nullable = false)
  private String newsId;

  @Column(name = "title", nullable = false)
  private String title;

  @Column(name = "content", length = 200)
  private String content;

  @Column(name = "published_at")
  private LocalDateTime publishedAt;

  @Column(name = "enveloped_at")
  private LocalDateTime envelopedAt;

  @Column(name = "dateline")
  private String dateline;

  @Column(name = "provider")
  private String provider;

  @Column(name = "category")
  private String category;

  @Column(name = "category_incident")
  private String categoryIncident;

  @Column(name = "hilight")
  private String hilight;

  @Column(name = "byline")
  private String byline;

  @Column(name = "images")
  private String images;

  @Column(name = "images_caption")
  private String imagesCaption;

  @Column(name = "provider_subject")
  private String providerSubject;

  @Column(name = "subject_info")
  private String subjectInfo;

  @Column(name = "subject_info1")
  private String subjectInfo1;

  @Column(name = "subject_info2")
  private String subjectInfo2;

  @Column(name = "subject_info3")
  private String subjectInfo3;

  @Column(name = "subject_info4")
  private String subjectInfo4;

  @Column(name = "provider_news_id")
  private String providerNewsId;

  @Column(name = "publisher_code")
  private String publisherCode;

  @Column(name = "provider_link_page")
  private String providerLinkPage;

  @Column(name = "printing_page")
  private String printingPage;

  @Column(name = "tms_raw_stream")
  private String tmsRawStream;

  @OneToMany(mappedBy = "rawNews", cascade = CascadeType.ALL, orphanRemoval = true)
  private List<BatchJobRawNews> batchJobRawNews = new ArrayList<>();

  @OneToOne(mappedBy = "rawNews", cascade = CascadeType.ALL, orphanRemoval = true)
  private FilteredNews filteredNews;
}
```

## FilteredNews


```java
package com.funa.batchapp.news.entity;

import com.funa.common.entity.BaseEntity;
import jakarta.persistence.*;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
@Entity
@Table(name = "batch_biz_filtered_news")
public class FilteredNews extends BaseEntity {

  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  private Long id;

  @Column(name = "title", nullable = false)
  private String title;

  @Column(name = "tms_raw_stream")
  private String tmsRawStream;

  @OneToOne
  @JoinColumn(name = "raw_news_id", unique = true)
  private RawNews rawNews;
}
```

## BatchJobRawNews

```java
package com.funa.batchapp.news.entity;

import com.funa.batchapp.job.BatchJobExecution;
import com.funa.common.entity.BaseEntity;
import jakarta.persistence.*;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Getter
@Setter
@NoArgsConstructor
@Entity
@Table(
    name = "batch_biz_batch_job_raw_news",
    uniqueConstraints = {@UniqueConstraint(columnNames = {"batch_job_id", "raw_news_id"})})
public class BatchJobRawNews extends BaseEntity {

  @Id
  @GeneratedValue(strategy = GenerationType.IDENTITY)
  private Long id;

  @ManyToOne
  @JoinColumn(name = "batch_job_id", nullable = false)
  private BatchJobExecution batchJob;

  @ManyToOne
  @JoinColumn(name = "raw_news_id", nullable = false)
  private RawNews rawNews;
}
```

## batch_job_execution

```sql
create table batch_job_execution
(
    job_execution_id bigint    not null
        primary key,
    version          bigint,
    job_instance_id  bigint    not null
        constraint job_inst_exec_fk
            references public.batch_job_instance,
    create_time      timestamp not null,
    start_time       timestamp,
    end_time         timestamp,
    status           varchar(10),
    exit_code        varchar(2500),
    exit_message     varchar(2500),
    last_updated     timestamp
);

```